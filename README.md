# SweepGraph

Layered "sweeps" that turn any text corpus into a Neo4j-ready knowledge graph.

**What it is:** General-purpose scaffolding for running iterative sweeps over the same corpus to progressively extract nodes/relationships and import them into Neo4j. Works with Gemini 2.5 Pro or any LLM of choice.

---

## Quick start

### 1. Install Prerequisites

Before cloning the repo, make sure these prerequisites are in place:

- **Docker** – Install Docker Desktop following the official guide: https://docs.docker.com/get-docker/
- **Python 3.11+** – Download installers from the Python website: https://www.python.org/downloads/
- **Gemini API access** – Create an API key in Google AI Studio: https://ai.google.dev/gemini-api/docs/get-started

Once Python is available you can grab the `uv` package manager (optional but recommended for this project):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

You will also need a Neo4j instance. Pick whichever option fits your workflow:

**Option A: Neo4j Desktop (Recommended for beginners)**
1. Download from https://neo4j.com/download/
2. Install and create a new database
3. Start the database
4. Note your connection details (bolt://localhost:7687)

**Option B: Docker (Recommended for developers)**
```bash
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/your_password \
    neo4j:latest
```

**Option C: Neo4j Aura (Cloud)**
1. Go to https://neo4j.com/cloud/aura/
2. Create a free instance
3. Note your connection URI and credentials

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - Add your Neo4j connection details
# - Add your Google Gemini API key
```

Get a Gemini API key: https://ai.google.dev/gemini-api/docs/get-started

### 3. Install Dependencies

```bash
# Install Python packages
uv sync
```

### 4. Add Your Corpus

```bash
# Copy your text corpus to data/raw/
cp /path/to/your/corpus.txt data/raw/corpus.txt

# Or PDF/DOCX - update paths in sweeps as needed
```

---

## Frontend (Streamlit UI)

Explore, edit, and monitor your graph with a lightweight, schema-agnostic UI. The UI discovers labels and relationship types from your Neo4j database and reads environment variables from `.env` via `python-dotenv`.

Run the UI:

```bash
streamlit run frontend/app.py
```

Pages:
- **Explorer**: Filter by label, inspect node properties and sample relationships.
- **Editor**: Create/Delete relationships between nodes by `id` (nodes are read-only by default).
- **Dashboard**: Quick stats (node/relationship counts, top relationship types).

Environment expected in `.env` (project root):

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password_here
```

Theme: tweak `frontend/.streamlit/config.toml`.

---

## Your first sweep

A "sweep" is a systematic pass that extracts specific elements from your corpus.

### Step 1: Create Your First Sweep

```bash
# Copy the template
cp scripts/templates/sweep_template.py scripts/sweep01_structure.py

# Copy the prompt template
cp prompts/v5/templates/prompt_template.txt prompts/v5/01_structure_extraction.txt
```

### Step 2: Customize the prompt

Edit `prompts/v5/01_structure_extraction.txt`:

```
You are analyzing a text corpus to extract document structure.

# Task
Extract the hierarchical structure of the thesis:
- Thesis title
- All chapters with numbers and titles
- All sections within each chapter
- All subsections

# Output Format
{
  "nodes": [
    {
      "id": "thesis:main",
      "labels": ["Thesis"],
      "properties": {
        "name": "Thesis Title Here",
        "author": "Your Name",
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
1. Extract ALL chapters
2. Extract ALL major sections
3. Preserve hierarchy
4. Use consistent ID patterns
```

### Step 3: Run Your First Sweep

```bash
# Run the sweep
uv run python scripts/sweep01_structure.py

# Check output
cat output/neo4j_ready/sweep01_structure.json
```

### Step 4: Import to Neo4j

```bash
# Import the data
uv run python scripts/import_to_neo4j.py output/neo4j_ready/sweep01_structure.json
```

### Step 5: Query your graph

Open Neo4j Browser (http://localhost:7474) and run:

```cypher
// See all nodes
MATCH (n)
RETURN n
LIMIT 50

// Example query: Structure
MATCH path = (t)-[:CONTAINS*]->(n)
RETURN path
```

---

## Creating more sweeps

### Recommended Sweep Sequence

1. **Sweep 1: Structure** - Chapters, sections, hierarchy
2. **Sweep 2: Concepts** - Key concepts/terms
3. **Sweep 3: Claims** - Key statements
4. **Sweep 4: Evidence** - Supporting evidence
5. **Sweep 5: Citations** - Citation network
6. **Sweep 6: Relationships** - Connect concepts and claims
7. **Sweep 7+**: Analysis sweeps (gaps, chains, etc.)

### Sweep Template

Each sweep should:
1. Have a clear, specific purpose
2. Use a numbered naming convention (`sweepNN_description.py`)
3. Have a corresponding prompt file (`NN_description.txt`)
4. Output to `output/neo4j_ready/sweepNN_description.json`
5. Be documented in `docs/sweeps/`

---

## Neo4j Query Examples

### Find All Concepts
```cypher
MATCH (c:Concept)
RETURN c.name, c.tier
ORDER BY c.tier, c.name
```

### Find Arguments with Evidence
```cypher
MATCH (e:Evidence)-[:SUPPORTS]->(a:Argument)
RETURN a.name, count(e) as evidence_count
ORDER BY evidence_count DESC
```

### Find Citation Network
```cypher
MATCH (c:Citation)<-[:CITES]-(content)
RETURN c.name, count(content) as times_cited
ORDER BY times_cited DESC
```

### Find Gaps
```cypher
// Arguments without evidence
MATCH (a:Argument)
WHERE NOT exists((a)<-[:SUPPORTS]-())
RETURN a.name
```

---

## Project Structure

```
SweepGraph/
├── README.md                  # This file
├── .env.example              # Configuration template
├── pyproject.toml            # Python dependencies
│
├── scripts/
│   ├── sweep*.py             # Extraction sweeps
│   ├── import_to_neo4j.py   # Import to database
│   ├── templates/            # Script templates
│   └── utils/                # Shared utilities
│
├── prompts/v5/
│   ├── *.txt                 # Extraction prompts
│   └── templates/            # Prompt templates
│
├── output/
│   ├── neo4j_ready/          # Import-ready JSON
│   ├── json/                 # Merged graphs
│   └── logs/                 # Execution logs
│
├── data/
│   ├── raw/                  # Your thesis text
│   └── registry/             # ID registries
│
└── docs/
    ├── guides/               # How-to guides
    ├── production/           # Formal documentation
    └── sweeps/               # Sweep reports
```

---

## Best Practices

### Sweep Development

1. **Start small**: Extract one thing at a time
2. **Test prompts**: Verify JSON output before importing
3. **Use IDs consistently**: Follow pattern `type:descriptive_slug`
4. **Track confidence**: Mark high/medium/low confidence
5. **Document sweeps**: Note what worked and what didn't

### Neo4j Management

1. **Backup regularly**: Export your database
2. **Test queries**: Verify data quality after imports
3. **Use constraints**: Create uniqueness constraints on IDs
4. **Monitor performance**: Watch for slow queries

### Quality Assurance

1. **Check for orphans**: Find disconnected nodes
2. **Validate relationships**: Ensure logical connections
3. **Track coverage**: Monitor % of content extracted
4. **Review confidence**: Focus on high-confidence data

---

## Common Issues

### "Neo4j connection refused"
- Start your Neo4j database
- Check credentials in `.env`
- Verify port 7687 is open

### "Gemini API error"
- Check your API key in `.env`
- Verify you have API credits
- Check rate limits

### "JSON parsing error"
- Review Gemini output in logs
- Improve prompt specificity
- Add more examples to prompt

### "Empty results"
- Check thesis text loaded correctly
- Verify prompt instructions are clear
- Review log files for errors

---

## Advanced Features

### Merge All Sweeps

```bash
# Combine all sweep files into one
python scripts/merge_all_sweeps.py
```

### Export Graph

```bash
# Export current database state
python scripts/export_graph.py
```

### Validate Ontology

```bash
# Check schema compliance
python scripts/validate_ontology.py
```

---

## Getting Help

### Resources

- **SweepGraph Documentation**: See `docs/` directory
- **Neo4j Documentation**: https://neo4j.com/docs/
- **Gemini API Docs**: https://ai.google.dev/docs

### Community

- Create issues for bugs
- Share your sweeps and prompts
- Contribute improvements

---

## License & Citation

### System Code
Open for academic use with attribution.

### Your Thesis Content
Remains your intellectual property. The graph extracts structure, not content.

### Suggested Citation

```
[Your Name] (2025). SweepGraph: Knowledge Graph Analysis
of [Your Thesis Title]. Built with SweepGraph methodology.
```

---

## Next Steps

1. ✅ Set up Neo4j database
2. ✅ Configure `.env` file
3. ✅ Place your thesis in `data/raw/`
4. ✅ Create your first sweep
5. ✅ Import and query
6. ✅ Iterate and refine

**Start small, test often, document everything!**

---

**Last Updated:** 2025-10-29
**Version:** 1.0.0
**Built with:** SweepGraph Methodology
