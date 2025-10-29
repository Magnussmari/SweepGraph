"""
SweepNN: [Description]

Purpose: [What this sweep extracts or enriches]
Output: output/neo4j_ready/sweepNN_description.json

Usage:
    python scripts/sweepNN_description.py
"""

import os
import json
import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv
from neo4j import GraphDatabase
from scripts.utils import setup_logger, get_timestamp

# Load environment
load_dotenv()

# Configure logging
logger = setup_logger("sweepNN", log_file="output/logs/sweepNN_description.log")

# Paths
CORPUS_TEXT_PATH = "data/raw/corpus.txt"  # Update with your corpus file
PROMPT_PATH = "prompts/v5/NN_description.txt"
OUTPUT_PATH = "output/neo4j_ready/sweepNN_description.json"

# Neo4j connection
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Gemini configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-exp")


def load_corpus_text():
    """Load corpus text from file."""
    logger.info("Loading corpus text from %s", CORPUS_TEXT_PATH)

    if not Path(CORPUS_TEXT_PATH).exists():
        logger.error("Corpus text file not found: %s", CORPUS_TEXT_PATH)
        raise FileNotFoundError(f"Please place your corpus text at {CORPUS_TEXT_PATH}")

    text = Path(CORPUS_TEXT_PATH).read_text()
    logger.info("Loaded %d characters", len(text))
    return text


def load_existing_nodes():
    """
    Load existing nodes from Neo4j for context.

    Modify this query based on what nodes you need for your sweep.
    """
    logger.info("Loading existing nodes from Neo4j")

    with driver.session() as session:
        result = session.run("""
            MATCH (n)
            RETURN labels(n)[0] as label, n.id as id, n.name as name
            LIMIT 100
        """)
        nodes = [dict(record) for record in result]

    logger.info("Loaded %d nodes", len(nodes))
    return nodes


def extract_with_gemini(corpus_text, existing_nodes, prompt_text):
    """Extract data using Gemini model."""
    logger.info("Preparing extraction prompt")

    # Build context
    context = f"""
# Existing Nodes (for reference)
{json.dumps(existing_nodes, indent=2)}

# Corpus Text
{corpus_text}
"""

    # Combine with prompt
    full_prompt = prompt_text + "\n\n" + context

    logger.info("Sending request to Gemini (context size: %d chars)", len(full_prompt))
    response = model.generate_content(full_prompt)

    logger.info("Received response from Gemini")
    return response.text


def parse_response(response_text):
    """Parse JSON from Gemini response."""
    logger.info("Parsing Gemini response")

    # Extract JSON from markdown code blocks if present
    if "```json" in response_text:
        start = response_text.find("```json") + 7
        end = response_text.find("```", start)
        json_text = response_text[start:end].strip()
    else:
        json_text = response_text.strip()

    try:
        data = json.loads(json_text)
        logger.info("Parsed JSON successfully")
        return data
    except json.JSONDecodeError as e:
        logger.error("Failed to parse JSON: %s", str(e))
        logger.debug("Response text: %s", response_text[:500])
        raise


def save_output(data):
    """Save output to JSON file."""
    logger.info("Saving output to %s", OUTPUT_PATH)

    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    logger.info("Output saved successfully")


def main():
    """Main execution."""
    logger.info("=== SweepNN: [Description] ===")

    try:
        # Load corpus text
        corpus_text = load_corpus_text()

        # Load existing nodes (optional)
        existing_nodes = load_existing_nodes()

        # Load prompt
        logger.info("Loading prompt from %s", PROMPT_PATH)

        if not Path(PROMPT_PATH).exists():
            logger.error("Prompt file not found: %s", PROMPT_PATH)
            raise FileNotFoundError(f"Please create prompt file at {PROMPT_PATH}")

        prompt_text = Path(PROMPT_PATH).read_text()

        # Extract with Gemini
        response = extract_with_gemini(corpus_text, existing_nodes, prompt_text)

        # Parse response
        data = parse_response(response)

        # Save output
        save_output(data)

        # Log statistics
        if "nodes" in data:
            logger.info("Total nodes extracted: %d", len(data["nodes"]))
        elif "relationships" in data:
            logger.info("Total relationships extracted: %d", len(data["relationships"]))
        elif "enrichments" in data:
            logger.info("Total enrichments: %d", len(data["enrichments"]))

        logger.info("=== SweepNN Complete ===")

    except Exception as e:
        logger.error("Error during sweep: %s", str(e), exc_info=True)
        raise

    finally:
        driver.close()


if __name__ == "__main__":
    main()
