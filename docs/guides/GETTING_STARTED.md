# Getting Started with SweepGraph

This guide walks you through creating your first knowledge graph from your thesis.

---

## Overview

The SweepGraph methodology involves:

1. **Extraction**: Use AI to extract structured data from thesis text
2. **Import**: Load extracted data into Neo4j graph database
3. **Analysis**: Query and visualize your thesis structure
4. **Refinement**: Identify gaps and improve iteratively

---

## Phase 1: Setup (15 minutes)

### Install Neo4j

**Mac (Homebrew)**:
```bash
brew install neo4j
neo4j start
```

**Windows/Linux**: Download Neo4j Desktop from https://neo4j.com/download/

**Docker**:
```bash
docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:latest
```

### Install Python Dependencies

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### Configure Environment

```bash
# Copy template
cp .env.example .env

# Edit .env
nano .env  # or use your favorite editor
```

Add:
- Neo4j URI (bolt://localhost:7687)
- Neo4j username (neo4j)
- Neo4j password (your password)
- Gemini API key (from https://makersuite.google.com/)

### Prepare Your Thesis

```bash
# Create data directory
mkdir -p data/raw

# Copy your thesis (plain text works best)
cp /path/to/thesis.txt data/raw/thesis.txt
```

**Tip**: Convert PDF/DOCX to TXT for best results:
- Mac: `textutil -convert txt thesis.docx`
- Linux: `pandoc thesis.pdf -o thesis.txt`
- Windows: Use Calibre or online converters

---

## Phase 2: First Extraction (30 minutes)

### Create Sweep 1: Structure

```bash
# Copy template
cp scripts/templates/sweep_template.py scripts/sweep01_structure.py

# Edit to customize paths
nano scripts/sweep01_structure.py
```

Update:
- `THESIS_TEXT_PATH` to your thesis location
- `OUTPUT_PATH` to `output/neo4j_ready/sweep01_structure.json`

### Create Prompt 1: Structure Extraction

```bash
# Copy template
cp prompts/v5/templates/prompt_template.txt prompts/v5/01_structure.txt

# Edit prompt
nano prompts/v5/01_structure.txt
```

Example structure prompt:

```
You are analyzing an academic thesis to extract its document structure.

# Task
Extract:
1. Thesis metadata (title, author, year)
2. All chapters (with numbers and titles)
3. All major sections (with parent chapters)

# Output Format
{
  "nodes": [
    {
      "id": "thesis:main",
      "labels": ["Thesis"],
      "properties": {
        "name": "Full Thesis Title",
        "author": "Author Name",
        "year": "2025",
        "confidence": "high"
      }
    },
    {
      "id": "chapter:1",
      "labels": ["Chapter"],
      "properties": {
        "name": "Chapter 1: Introduction",
        "number": 1,
        "confidence": "high"
      }
    }
  ],
  "relationships": [
    {
      "source_id": "thesis:main",
      "target_id": "chapter:1",
      "type": "CONTAINS",
      "properties": {}
    }
  ]
}

# Rules
1. Extract EVERY chapter mentioned
2. Use chapter numbers from the text
3. Maintain hierarchy (Thesis → Chapter → Section)
4. IDs must follow pattern: thesis:*, chapter:*, section:*
```

### Run Sweep 1

```bash
# Execute extraction
uv run python scripts/sweep01_structure.py

# Check logs
tail -f output/logs/sweep01_structure.log
```

Expected output:
- JSON file in `output/neo4j_ready/sweep01_structure.json`
- Log file showing extraction progress
- Statistics (nodes extracted, confidence levels)

### Import to Neo4j

```bash
# Import data
uv run python scripts/import_to_neo4j.py output/neo4j_ready/sweep01_structure.json
```

### Verify in Neo4j Browser

1. Open http://localhost:7474
2. Login with your credentials
3. Run query:

```cypher
MATCH (n)
RETURN n
```

You should see your thesis structure!

---

## Phase 3: Expand Your Graph (1-2 hours)

### Sweep 2: Extract Concepts

Create `scripts/sweep02_concepts.py` and `prompts/v5/02_concepts.txt`.

Example prompt:

```
Extract key theoretical concepts from the thesis.

Include:
- Main theoretical frameworks
- Key terms and definitions
- Conceptual categories

Output as Concept nodes with properties:
- name: Concept name
- definition: Brief definition
- tier: tier_0 (foundational), tier_1 (main), tier_2 (supporting)
```

### Sweep 3: Extract Arguments

Create `scripts/sweep03_arguments.py` and `prompts/v5/03_arguments.txt`.

Example prompt:

```
Extract main arguments and claims.

Include:
- Central thesis claims
- Chapter arguments
- Sub-arguments supporting main claims

Output as Argument nodes with properties:
- name: Argument statement
- chapter: Chapter number
- type: main_thesis | chapter_claim | sub_argument
```

### Sweep 4: Extract Evidence

Create `scripts/sweep04_evidence.py` and `prompts/v5/04_evidence.txt`.

### Sweep 5: Connect Evidence to Arguments

Create `scripts/sweep05_relationships.py` to:
- MATCH existing Arguments and Evidence
- CREATE SUPPORTS relationships between them

---

## Phase 4: Analysis & Refinement (ongoing)

### Find Gaps

```cypher
// Arguments without evidence
MATCH (a:Argument)
WHERE NOT exists((a)<-[:SUPPORTS]-())
RETURN a.name, a.chapter
ORDER BY a.chapter
```

### Check Coverage

```cypher
// Evidence per chapter
MATCH (e:Evidence)
RETURN e.chapter, count(e) as evidence_count
ORDER BY e.chapter
```

### Visualize Structure

```cypher
// Full thesis hierarchy
MATCH path = (t:Thesis)-[:CONTAINS*]->(n)
RETURN path
```

---

## Tips for Success

### Prompt Engineering

1. **Be specific**: "Extract arguments" → "Extract claim statements that assert a position"
2. **Provide examples**: Show 2-3 good examples in prompt
3. **Set constraints**: Specify ID patterns, required properties
4. **Iterate**: Refine prompts based on output quality

### Sweep Strategy

1. **Start broad**: Structure, concepts, arguments
2. **Add detail**: Evidence, citations, definitions
3. **Create relationships**: Connect nodes meaningfully
4. **Analyze**: Find gaps, validate logic
5. **Refine**: Fix issues, add missing elements

### Quality Checks

After each sweep:
1. **Check JSON validity**: Does it parse?
2. **Review confidence scores**: How many low-confidence items?
3. **Verify IDs**: Consistent format?
4. **Test import**: Does it load to Neo4j?
5. **Query results**: Does output make sense?

---

## Common Workflows

### Daily Development

```bash
# 1. Create new sweep
cp scripts/templates/sweep_template.py scripts/sweepNN_description.py

# 2. Create prompt
nano prompts/v5/NN_description.txt

# 3. Run sweep
uv run python scripts/sweepNN_description.py

# 4. Import to Neo4j
uv run python scripts/import_to_neo4j.py output/neo4j_ready/sweepNN_description.json

# 5. Query and verify
# (Use Neo4j Browser)
```

### Backup & Export

```bash
# Export current state
uv run python scripts/export_graph.py

# Results in: output/json/graph_export_YYYYMMDD_HHMMSS.json
```

### Reset & Start Over

```cypher
// In Neo4j Browser: Delete all nodes and relationships
MATCH (n)
DETACH DELETE n
```

---

## Next Steps

1. ✅ Complete structural extraction
2. ✅ Extract concepts and arguments
3. ✅ Add evidence and citations
4. ✅ Create relationship sweeps
5. ✅ Analyze for gaps
6. ✅ Iterate and refine

---

## Troubleshooting

### Neo4j Won't Start
- Check if port 7687 is in use: `lsof -i :7687`
- Try restarting: `neo4j restart`
- Check logs: `neo4j console`

### Gemini API Errors
- Verify API key is valid
- Check rate limits (free tier: 60 requests/minute)
- Reduce context size if hitting limits

### Import Fails
- Validate JSON: `python -m json.tool < output/file.json`
- Check for duplicate IDs
- Verify all referenced IDs exist

### Low Quality Extractions
- Add more examples to prompts
- Be more specific about what to extract
- Provide negative examples (what NOT to do)
- Reduce scope (extract less at once)

---

**Ready to build your knowledge graph!** 🚀
