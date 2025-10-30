"""Bootstrap a demo corpus and structure sweep output for instant exploration.

Running this script creates a sample corpus, generates a structure sweep JSON,
and optionally imports it into the configured Neo4j instance.

Usage:
    uv run python scripts/utilities/quickstart_demo.py
    uv run python scripts/utilities/quickstart_demo.py --skip-import
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Tuple

# Ensure repository root is on sys.path when executed directly
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.utils import setup_logger

LOGGER = setup_logger("quickstart", log_file="output/logs/quickstart_demo.log")
SAMPLE_CORPUS_PATH = Path("data/raw/sample_corpus.txt")
OUTPUT_JSON_PATH = Path("output/neo4j_ready/sample_sweep01_structure.json")
DOCUMENT_ID = "document:sample_corpus"
SWEEP_ID = "sweep01_demo_structure"


def slugify(text: str) -> str:
    """Convert text into a filesystem and Neo4j friendly slug."""
    slug = []
    for char in text.lower():
        if char.isalnum():
            slug.append(char)
        elif not slug or slug[-1] != "_":
            slug.append("_")
    cleaned = "".join(slug).strip("_")
    return cleaned or "item"


def ensure_sample_corpus() -> str:
    """Ensure the sample corpus exists and return its contents."""
    if not SAMPLE_CORPUS_PATH.exists():
        LOGGER.error("Sample corpus missing at %s", SAMPLE_CORPUS_PATH)
        raise FileNotFoundError(
            "Sample corpus not found. Make sure the repository files are intact."
        )
    text = SAMPLE_CORPUS_PATH.read_text().strip()
    LOGGER.info("Loaded sample corpus (%d characters)", len(text))
    return text


def parse_corpus(text: str) -> Tuple[List[dict], List[dict]]:
    """Generate nodes and relationships that mimic a structure sweep."""
    nodes: List[dict] = []
    relationships: List[dict] = []

    document_node = {
        "labels": ["Document"],
        "properties": {
            "id": DOCUMENT_ID,
            "name": "Sample Corpus",
            "title": "Decarbonizing Urban Transport",
            "sweep_id": SWEEP_ID,
            "source": "quickstart-demo"
        }
    }
    nodes.append(document_node)

    current_chapter = None
    current_section = None
    section_buffer: List[str] = []

    def finalize_section():
        nonlocal section_buffer, current_section
        if not current_section:
            return
        summary = " ".join(line.strip() for line in section_buffer if line.strip())
        if summary:
            current_section["properties"]["summary"] = summary
        section_buffer = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.lower().startswith("chapter "):
            finalize_section()
            chapter_slug = slugify(line)
            chapter_id = f"chapter:{chapter_slug}"
            chapter_node = {
                "labels": ["Chapter"],
                "properties": {
                    "id": chapter_id,
                    "name": line,
                    "sweep_id": SWEEP_ID,
                    "order": line.split(":")[0].strip().replace("Chapter ", "")
                }
            }
            nodes.append(chapter_node)
            relationships.append({
                "source_id": DOCUMENT_ID,
                "target_id": chapter_id,
                "type": "CONTAINS",
                "properties": {"sweep_id": SWEEP_ID}
            })
            current_chapter = chapter_node
            current_section = None
            continue

        if line.lower().startswith("section "):
            finalize_section()
            if not current_chapter:
                LOGGER.warning("Encountered section before chapter: %s", line)
                continue
            section_slug = slugify(line)
            section_id = f"section:{section_slug}"
            section_node = {
                "labels": ["Section"],
                "properties": {
                    "id": section_id,
                    "name": line,
                    "chapter_id": current_chapter["properties"]["id"],
                    "sweep_id": SWEEP_ID,
                    "order": line.split(":")[0].strip().replace("Section ", "")
                }
            }
            nodes.append(section_node)
            relationships.append({
                "source_id": current_chapter["properties"]["id"],
                "target_id": section_id,
                "type": "CONTAINS",
                "properties": {"sweep_id": SWEEP_ID}
            })
            current_section = section_node
            continue

        if current_section:
            section_buffer.append(line)

    finalize_section()
    LOGGER.info("Generated %d nodes and %d relationships", len(nodes), len(relationships))
    return nodes, relationships


def write_output(nodes: List[dict], relationships: List[dict]) -> Path:
    """Write the generated sweep output to JSON."""
    OUTPUT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "sweep_id": SWEEP_ID,
        "nodes": nodes,
        "relationships": relationships
    }
    with OUTPUT_JSON_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    LOGGER.info("Wrote demo sweep to %s", OUTPUT_JSON_PATH)
    return OUTPUT_JSON_PATH


def import_into_neo4j(json_path: Path) -> bool:
    """Import the generated JSON into Neo4j if credentials are configured."""
    try:
        from scripts.import_to_neo4j import Neo4jImporter
    except Exception as exc:  # pragma: no cover - defensive
        LOGGER.error("Unable to load Neo4j importer: %s", exc)
        return False

    importer = Neo4jImporter()
    try:
        importer.import_file(str(json_path))
    except Exception as exc:  # pragma: no cover - connection issues vary
        LOGGER.error(
            "Neo4j import failed. Verify Neo4j is running and credentials are correct."
        )
        LOGGER.debug("Import error: %s", exc, exc_info=True)
        return False
    finally:
        importer.close()

    LOGGER.info("Demo data imported into Neo4j. Open http://localhost:7474 to explore.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Run the SweepGraph quickstart demo")
    parser.add_argument(
        "--skip-import",
        action="store_true",
        help="Generate files without importing into Neo4j"
    )
    args = parser.parse_args()

    corpus_text = ensure_sample_corpus()
    nodes, relationships = parse_corpus(corpus_text)
    json_path = write_output(nodes, relationships)

    if args.skip_import:
        LOGGER.info("Skipping Neo4j import as requested.")
        return

    success = import_into_neo4j(json_path)
    if not success:
        LOGGER.info("Quickstart demo JSON is ready. Import manually with: \n"
                    "    uv run python scripts/import_to_neo4j.py %s",
                    json_path)


if __name__ == "__main__":
    main()
