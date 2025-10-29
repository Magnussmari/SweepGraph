# 📋 COPY THIS ENTIRE README INTO YOUR LLM OF CHOICE

**Yes, you read that right.** This README is designed to be both:
- 📖 **Traditional documentation** (read it on GitHub)
- 🤖 **An interactive AI guide** (paste it into Claude, ChatGPT, Perplexity, etc.)

When you paste this README into an LLM, it becomes your personal guide through SweepGraph. The LLM can answer questions, help you debug issues, customize sweeps for your specific corpus, and guide you step-by-step through knowledge graph extraction.

**Try it now:** Copy this entire page and paste it into your favorite LLM, then ask questions like:
- "I have a 300-page thesis to analyze, where do I start?"
- "How do I extract argument structures from my research paper?"
- "My Neo4j connection isn't working, help me debug"
- "What's the best sweep sequence for legal documents?"
- "Walk me through creating my first custom sweep"

### 💬 Example Interaction

**You:** *[Paste this README into Claude/ChatGPT]*
"Hi! I have a PhD thesis on climate policy that I want to turn into a knowledge graph. I've never used Neo4j before."

**LLM:** "Perfect! SweepGraph is designed for exactly this use case. Let me guide you through the setup and your first extraction.

**Your situation:**
- PhD thesis (likely 200-400 pages with complex structure)
- Climate policy domain (lots of concepts, arguments, evidence, citations)
- New to Neo4j (we'll start with the Desktop version - easiest)

**Here's your personalized plan:**

**Phase 1: Setup (30-45 minutes)**
1. Install Neo4j Desktop (simplest for beginners)
2. Install Python 3.11+ and uv package manager
3. Get a Gemini API key (free tier works for testing)
4. Clone the repo and configure .env

**Phase 2: Your First Sweep (1-2 hours)**
1. Extract thesis structure (chapters, sections)
2. Import to Neo4j and visualize
3. Run your first Cypher queries

**Phase 3: Progressive Extraction (iterative)**
1. Sweep for climate policy concepts
2. Extract key arguments and claims
3. Map evidence to arguments
4. Build citation network
5. Discover gaps and connections

**Before we start, a few questions:**
- Do you have your thesis as a .txt, .pdf, or .docx file?
- Are you on Mac, Windows, or Linux?
- Do you want to analyze the entire thesis or just specific chapters?

Let me know and I'll walk you through each step!"

**That's the power of this approach** - the README becomes your expert guide.

---

## 🤖 Instructions for AI Assistants

**If you are an AI assistant reading this**, you have been given the complete contents of the **SweepGraph** repository—a system for turning text corpora into Neo4j knowledge graphs through progressive, layered extraction sweeps.

**Your Role:**
- Guide users through SweepGraph based on their corpus type, goals, and technical experience
- Help debug Neo4j connection issues, API errors, and JSON parsing problems
- Assist with prompt engineering for optimal extraction quality
- Explain Neo4j/Cypher concepts in accessible terms
- Customize sweep sequences for different document types
- Be conversational and helpful, not robotic or overly technical

**When a user pastes this, start by asking:**
1. What type of document/corpus do they want to analyze?
   - Academic thesis/dissertation
   - Research papers
   - Legal documents
   - Technical documentation
   - Books or long-form content
   - Other
2. Their experience level with:
   - Neo4j and graph databases
   - Python/scripting
   - LLM prompt engineering
3. Their specific goals:
   - Understanding document structure
   - Extracting arguments and evidence
   - Building citation networks
   - Finding gaps or inconsistencies
   - Creating interactive visualizations

**Then guide them to the appropriate path.**

**Common User Scenarios and How to Help:**

1. **Complete Beginner (Never used Neo4j or graphs)**
   - Start with Neo4j Desktop (easiest option)
   - Walk through .env setup step-by-step
   - Explain what a "node" and "relationship" are
   - Use the structure sweep first (simplest, visual results)
   - Show them the Streamlit UI for exploration
   - Set realistic expectations: first sweep takes 1-2 hours

2. **Research/Academic User (Has data, unclear on graphs)**
   - Focus on their research questions
   - Map research questions to sweep sequences
   - Explain how graphs reveal hidden connections
   - Recommend sweep order for their domain:
     - Thesis: Structure → Concepts → Claims → Evidence → Citations
     - Papers: Concepts → Methods → Results → Citations
     - Legal: Structure → Definitions → Precedents → Arguments
   - Help with prompt engineering for their specific terminology

3. **Technical User (Knows Python/databases, new to graphs)**
   - Brief overview of graph thinking vs. relational
   - Point to Cypher query examples
   - Explain sweep template architecture
   - They can move fast - focus on customization
   - Show advanced features (merge, export, validation)

4. **Stuck on Technical Issues**
   - **Neo4j won't connect**: Check Docker status, verify .env credentials, test port 7687
   - **Gemini API errors**: Verify API key, check rate limits, test with curl
   - **JSON parsing fails**: Review logs, show example of valid JSON, improve prompt specificity
   - **Empty results**: Check corpus loading, verify prompt clarity, add examples to prompt
   - **Slow performance**: Explain Neo4j indexes, recommend constraints, optimize queries

5. **Domain-Specific Adaptations**
   - **Legal documents**: Extract precedents, statutes, arguments, judicial reasoning
   - **Scientific papers**: Methods, results, hypotheses, experimental design
   - **Technical docs**: APIs, dependencies, configurations, workflows
   - **Books/literature**: Characters, themes, plot structure, narrative arcs
   - **Business docs**: Processes, stakeholders, requirements, risks

**Key Files You Can Reference:**
- `.env.example` - Configuration template
- `scripts/templates/sweep_template.py` - Sweep script template
- `prompts/v5/templates/prompt_template.txt` - Prompt template
- `scripts/import_to_neo4j.py` - Import utility
- `frontend/app.py` - Streamlit UI entry point

**Your Tone:**
- Practical and clear, not academic
- Patient with beginners
- Honest about time/effort required
- Enthusiastic about graph insights
- Debugging-focused when users are stuck

**Remember:**
- Always ask clarifying questions first
- Don't assume technical knowledge
- Use analogies for graph concepts
- Provide concrete examples from their domain
- Offer to walk through code step-by-step
- Celebrate small wins ("Great! Your first nodes are in Neo4j!")

---

# 🕸️ SweepGraph: Progressive Knowledge Graph Extraction

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](#)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Neo4j](https://img.shields.io/badge/neo4j-5.0+-008CC1.svg)](https://neo4j.com/)

**Transform any text corpus into an interactive, queryable knowledge graph** 🚀

Turn hundreds of pages of dense text into a structured Neo4j graph that reveals hidden connections, identifies gaps, and makes your content interactive and explorable.

---

## 📖 What Is SweepGraph?

**SweepGraph is a methodology and scaffolding for progressive knowledge extraction.**

Instead of trying to extract everything at once (and failing), SweepGraph uses **layered "sweeps"**—each sweep focuses on extracting one specific type of information:

1. **Sweep 1:** Extract document structure (chapters, sections)
2. **Sweep 2:** Identify key concepts and terminology
3. **Sweep 3:** Extract claims and arguments
4. **Sweep 4:** Map supporting evidence
5. **Sweep 5:** Build citation networks
6. **Sweep 6:** Connect concepts to claims
7. **Sweep 7+:** Analytical sweeps (find gaps, trace reasoning chains)

**Each sweep builds on previous ones**, progressively enriching your knowledge graph.

**Why this works:**
- ✅ Focused prompts get better LLM results
- ✅ Iterative process catches what early sweeps miss
- ✅ You validate and refine incrementally
- ✅ Works with any text corpus (thesis, papers, books, docs)
- ✅ Uses any LLM (Gemini, Claude, GPT, local models)

---

## 🎯 What Can You Build?

**Academic Research:**
- Turn your PhD thesis into an interactive graph
- Extract argument structures from papers
- Build citation networks automatically
- Find gaps in literature reviews
- Trace evidence chains

**Legal Analysis:**
- Extract case law precedents
- Map statutory relationships
- Identify conflicting interpretations
- Build argument dependency graphs

**Technical Documentation:**
- Extract API relationships
- Map system dependencies
- Document configuration flows
- Create interactive tech docs

**Books & Literature:**
- Character relationship maps
- Theme and motif networks
- Plot structure analysis
- Narrative arc visualization

**Any Structured Text:**
- If it has concepts, relationships, or structure, SweepGraph can extract it

---

## 🚀 Quick Start (30 Minutes)

### Step 0: Install Prerequisites

**You'll need:**
- **Docker Desktop** → https://docs.docker.com/get-docker/
- **Python 3.11+** → https://www.python.org/downloads/
- **Gemini API key** → https://ai.google.dev/gemini-api/docs/get-started (free tier works)

**Install uv (recommended Python package manager):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Choose your Neo4j setup:**

**Option A: Neo4j Desktop (Easiest for beginners)**
1. Download from https://neo4j.com/download/
2. Install and create a new database
3. Start the database
4. Note: `bolt://localhost:7687` (default connection)

**Option B: Docker (Fastest for developers)**
```bash
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/your_password \
    neo4j:latest
```

**Option C: Neo4j Aura (Cloud, free tier)**
1. Create account at https://neo4j.com/cloud/aura/
2. Create free instance
3. Save connection URI and credentials

### Step 1: Clone and Configure

```bash
# Clone the repository
git clone https://github.com/Magnussmari/SweepGraph.git
cd SweepGraph

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
# - GOOGLE_API_KEY (Gemini)
nano .env  # or your editor of choice
```

### Step 2: Install Dependencies

```bash
# Install Python packages
uv sync

# Or with pip
pip install -r requirements.txt
```

### Step 3: Add Your Text Corpus

```bash
# Copy your thesis/document to data/raw/
cp /path/to/your/thesis.txt data/raw/corpus.txt

# Or PDF/DOCX (update paths in sweep scripts as needed)
```

### Step 4: Your First Sweep (Structure Extraction)

```bash
# Copy templates
cp scripts/templates/sweep_template.py scripts/sweep01_structure.py
cp prompts/v5/templates/prompt_template.txt prompts/v5/01_structure_extraction.txt

# Run the sweep (extracts chapters, sections, hierarchy)
uv run python scripts/sweep01_structure.py

# Import to Neo4j
uv run python scripts/import_to_neo4j.py output/neo4j_ready/sweep01_structure.json
```

### Step 5: Explore Your Graph

**Open Neo4j Browser:** http://localhost:7474

```cypher
// See all nodes
MATCH (n)
RETURN n
LIMIT 50

// View structure hierarchy
MATCH path = (t)-[:CONTAINS*]->(n)
RETURN path
```

**Or use the Streamlit UI:**
```bash
streamlit run frontend/app.py
```

Navigate to: http://localhost:8501

**🎉 You now have your first knowledge graph!**

---

## 🎼 The Progressive Sweep Philosophy

**Traditional Approach (Doesn't Work):**
```
You → "Extract everything from this 300-page thesis"
      ↓
   LLM tries and fails
      ↓
   Mediocre, incomplete results
```

**SweepGraph Approach (Works):**
```
Sweep 1 → Extract structure (chapters, sections)
Sweep 2 → Extract concepts (clear nodes now)
Sweep 3 → Extract claims (linked to sections)
Sweep 4 → Extract evidence (linked to claims)
Sweep 5 → Extract citations (complete context)
Sweep 6 → Connect concepts to claims
Sweep 7 → Analytical queries (find gaps, chains)
          ↓
   Rich, validated knowledge graph
```

**Why layered sweeps work:**
- **Focus**: Each prompt has one clear job
- **Context**: Later sweeps build on earlier structure
- **Quality**: You validate incrementally
- **Flexibility**: Skip, reorder, or add sweeps as needed
- **Debuggable**: Easy to see where issues arise

---

## 📚 Recommended Sweep Sequences

### For Academic Thesis/Dissertation

**Phase 1: Foundation (Sweeps 1-2)**
1. **Structure Sweep** - Chapters, sections, subsections
2. **Concept Sweep** - Key terms, definitions, theories

**Phase 2: Argumentation (Sweeps 3-4)**
3. **Claim Sweep** - Arguments, hypotheses, assertions
4. **Evidence Sweep** - Data, quotes, studies supporting claims

**Phase 3: Context (Sweep 5)**
5. **Citation Sweep** - References, authors, citation relationships

**Phase 4: Integration (Sweeps 6-7)**
6. **Relationship Sweep** - Connect concepts, claims, evidence
7. **Gap Analysis Sweep** - Find unsupported arguments, orphaned evidence

**Timeline:** 1-2 weeks of iterative refinement

### For Research Papers

1. **Metadata** - Authors, institutions, keywords
2. **Concepts** - Key terms and definitions
3. **Methods** - Experimental design, data sources
4. **Results** - Findings and interpretations
5. **Citations** - Reference network

**Timeline:** 2-3 days per paper

### For Legal Documents

1. **Structure** - Sections, articles, clauses
2. **Definitions** - Legal terms and interpretations
3. **Precedents** - Case citations and reasoning
4. **Arguments** - Legal claims and rebuttals
5. **Relationships** - How precedents relate

**Timeline:** 1 week per significant document

### For Technical Documentation

1. **Components** - Systems, modules, services
2. **Dependencies** - What requires what
3. **Configurations** - Settings and parameters
4. **Workflows** - Processes and sequences
5. **APIs** - Endpoints and relationships

**Timeline:** 3-5 days

---

## 🎨 The Streamlit Frontend

**Explore, edit, and monitor your graph visually.**

```bash
streamlit run frontend/app.py
```

**Three main pages:**

### 🔍 Explorer
- Filter nodes by label (Concept, Claim, Evidence, etc.)
- View node properties
- Sample relationships
- Search functionality

### ✏️ Editor
- Create relationships between nodes
- Delete relationships
- Read-only node viewing (safety)
- Relationship property editing

### 📊 Dashboard
- Node count by label
- Relationship type distribution
- Top relationships
- Graph statistics
- Quality metrics

**Configuration:** Edit `frontend/.streamlit/config.toml` for theming

---

## 🛠️ Creating Custom Sweeps

### Anatomy of a Sweep

**1. The Python Script** (`scripts/sweepXX_description.py`)
- Loads your corpus
- Sends to LLM with prompt
- Parses JSON response
- Validates structure
- Saves to `output/neo4j_ready/`

**2. The Prompt** (`prompts/v5/XX_description.txt`)
- Clear task description
- Output format (JSON schema)
- Rules and constraints
- Examples (optional but helpful)

**3. The Output** (`output/neo4j_ready/sweepXX_description.json`)
```json
{
  "nodes": [
    {
      "id": "concept:climate_change",
      "labels": ["Concept"],
      "properties": {
        "name": "Climate Change",
        "definition": "Long-term shifts in global temperatures...",
        "tier": "core",
        "confidence": "high"
      }
    }
  ],
  "relationships": [
    {
      "source_id": "concept:climate_change",
      "target_id": "claim:anthropogenic_warming",
      "type": "RELATES_TO",
      "properties": {
        "strength": "strong"
      }
    }
  ]
}
```

### Sweep Best Practices

**1. Use Consistent ID Patterns**
```python
# Good
"id": "concept:climate_change"
"id": "chapter:01"
"id": "claim:main_hypothesis"

# Bad
"id": "cc"
"id": "1"
"id": "random_string_123"
```

**2. Add Confidence Scores**
```json
{
  "confidence": "high",  // or "medium", "low"
  "source": "section_3.2"
}
```

**3. Preserve Context**
```json
{
  "text_excerpt": "First 200 chars of relevant text...",
  "page": 42,
  "section": "chapter_3.2"
}
```

**4. Test Incrementally**
- Run sweep on small corpus first
- Check JSON output before importing
- Validate in Neo4j Browser
- Refine prompt based on results

---

## 📊 Neo4j Query Cookbook

### Basic Exploration

```cypher
// Count nodes by label
MATCH (n)
RETURN labels(n)[0] as label, count(n) as count
ORDER BY count DESC

// Count relationships by type
MATCH ()-[r]->()
RETURN type(r) as relationship, count(r) as count
ORDER BY count DESC

// Find orphaned nodes (no relationships)
MATCH (n)
WHERE NOT (n)--()
RETURN n.name, labels(n)
```

### Structure Analysis

```cypher
// Find deepest hierarchy paths
MATCH path = (t)-[:CONTAINS*]->(n)
WHERE NOT (n)-[:CONTAINS]->()
RETURN path
ORDER BY length(path) DESC
LIMIT 10

// Chapters with most subsections
MATCH (c:Chapter)-[:CONTAINS*]->(s)
RETURN c.name, count(s) as subsections
ORDER BY subsections DESC
```

### Argumentation Analysis

```cypher
// Claims with most evidence
MATCH (e:Evidence)-[:SUPPORTS]->(c:Claim)
RETURN c.name, count(e) as evidence_count, c.confidence
ORDER BY evidence_count DESC

// Claims without evidence (gaps!)
MATCH (c:Claim)
WHERE NOT (c)<-[:SUPPORTS]-(:Evidence)
RETURN c.name, c.section

// Evidence chains
MATCH path = (e:Evidence)-[:SUPPORTS]->(c:Claim)-[:SUPPORTS]->(h:Hypothesis)
RETURN path
```

### Citation Network

```cypher
// Most cited authors
MATCH (c:Citation)<-[:CITES]-(content)
RETURN c.author, c.year, count(content) as times_cited
ORDER BY times_cited DESC
LIMIT 20

// Co-citation network (authors cited together)
MATCH (c1:Citation)<-[:CITES]-(n)-[:CITES]->(c2:Citation)
WHERE id(c1) < id(c2)
RETURN c1.author, c2.author, count(n) as co_citations
ORDER BY co_citations DESC
LIMIT 50
```

### Concept Relationships

```cypher
// Core concepts (high connectivity)
MATCH (c:Concept)
RETURN c.name, c.tier,
       size((c)-[:RELATES_TO]-()) as relationships
ORDER BY relationships DESC
LIMIT 20

// Concept clusters
MATCH (c1:Concept)-[:RELATES_TO*..2]-(c2:Concept)
WHERE c1.tier = 'core'
RETURN c1.name, collect(distinct c2.name) as related_concepts

// Orphaned concepts (potentially missing relationships)
MATCH (c:Concept)
WHERE NOT (c)-[:RELATES_TO]-()
  AND NOT (c)<-[:HAS_CONCEPT]-()
RETURN c.name, c.definition
```

### Quality Assurance

```cypher
// Low confidence nodes
MATCH (n)
WHERE n.confidence = 'low'
RETURN labels(n)[0] as type, n.name, n.source
ORDER BY type

// Nodes missing required properties
MATCH (n:Concept)
WHERE n.definition IS NULL
RETURN n.name

// Duplicate IDs (shouldn't happen, but check)
MATCH (n)
WITH n.id as id, collect(n) as nodes
WHERE size(nodes) > 1
RETURN id, size(nodes) as duplicates
```

---

## 🐛 Troubleshooting Guide

### "Neo4j connection refused"

**Symptoms:** Can't import data, frontend won't connect

**Solutions:**
1. **Check Neo4j is running**
   ```bash
   # Docker users
   docker ps | grep neo4j

   # Desktop users: Check Neo4j Desktop UI
   ```

2. **Verify .env credentials**
   ```bash
   cat .env | grep NEO4J
   # Should match your Neo4j password
   ```

3. **Test connection manually**
   ```python
   from neo4j import GraphDatabase

   driver = GraphDatabase.driver(
       "bolt://localhost:7687",
       auth=("neo4j", "your_password")
   )
   driver.verify_connectivity()
   ```

4. **Check port 7687 is open**
   ```bash
   lsof -i :7687
   ```

### "Gemini API error"

**Symptoms:** Sweeps fail with API errors

**Solutions:**
1. **Verify API key**
   ```bash
   cat .env | grep GOOGLE_API_KEY
   # Copy key and test at https://aistudio.google.com
   ```

2. **Check rate limits**
   - Free tier: 60 requests/minute
   - Solution: Add delays between chunks

3. **Increase timeout**
   ```python
   # In sweep script
   response = model.generate_content(
       prompt,
       request_options={"timeout": 300}  # 5 minutes
   )
   ```

4. **Try smaller chunks**
   - Break corpus into smaller pieces
   - Process incrementally

### "JSON parsing error"

**Symptoms:** `JSONDecodeError` or invalid format

**Solutions:**
1. **Check LLM output logs**
   ```bash
   cat output/logs/sweep01_structure.log
   # Look for malformed JSON
   ```

2. **Improve prompt specificity**
   ```text
   # Add to prompt:
   CRITICAL: Output ONLY valid JSON. No markdown, no explanations.
   Start with { and end with }
   ```

3. **Add JSON schema to prompt**
   ```text
   # Include exact schema:
   {
     "nodes": [{"id": "string", "labels": ["string"], "properties": {}}],
     "relationships": [{"source_id": "string", "target_id": "string", "type": "string"}]
   }
   ```

4. **Use JSON repair libraries**
   ```python
   import json_repair

   repaired = json_repair.loads(llm_response)
   ```

### "Empty results"

**Symptoms:** Sweep runs but extracts nothing

**Solutions:**
1. **Verify corpus loaded**
   ```python
   # In sweep script, add:
   print(f"Loaded {len(corpus_text)} characters")
   print(corpus_text[:500])  # First 500 chars
   ```

2. **Check prompt clarity**
   - Add specific examples
   - Use explicit instructions
   - Test prompt in AI chat first

3. **Adjust context window**
   ```python
   # Send smaller chunks
   chunk_size = 10000  # characters
   chunks = [corpus_text[i:i+chunk_size]
             for i in range(0, len(corpus_text), chunk_size)]
   ```

4. **Review model selection**
   - Try different model (Claude, GPT-4, local)
   - Some models better at structured extraction

### "Slow performance"

**Symptoms:** Queries take forever, UI laggy

**Solutions:**
1. **Create indexes**
   ```cypher
   // In Neo4j Browser
   CREATE INDEX concept_name FOR (c:Concept) ON (c.name);
   CREATE INDEX claim_id FOR (c:Claim) ON (c.id);
   ```

2. **Add constraints**
   ```cypher
   CREATE CONSTRAINT unique_node_id
   FOR (n:Node) REQUIRE n.id IS UNIQUE;
   ```

3. **Optimize queries**
   ```cypher
   // Bad: Scans all nodes
   MATCH (n) WHERE n.name CONTAINS 'climate'

   // Good: Uses index
   MATCH (n:Concept) WHERE n.name CONTAINS 'climate'
   ```

4. **Use EXPLAIN and PROFILE**
   ```cypher
   PROFILE MATCH (c:Concept)-[r]->(n)
   RETURN c, r, n
   LIMIT 50
   ```

---

## 🎓 Advanced Techniques

### Merge Multiple Sweeps

Combine all sweep outputs into a single comprehensive graph:

```bash
python scripts/merge_all_sweeps.py
# Creates: output/json/merged_graph.json
```

### Export Current Graph State

Backup or version your graph:

```bash
python scripts/export_graph.py
# Creates: output/exports/graph_YYYYMMDD_HHMMSS.json
```

### Validate Against Ontology

Ensure your graph follows schema rules:

```bash
python scripts/validate_ontology.py
# Checks: required properties, valid relationships, orphans
```

### Custom Validation Rules

Add domain-specific validation:

```python
# scripts/custom_validation.py

def validate_argument_structure(tx):
    """Claims should have evidence or mark as hypothesis"""
    query = """
    MATCH (c:Claim)
    WHERE NOT (c)<-[:SUPPORTS]-(:Evidence)
      AND c.type <> 'hypothesis'
    RETURN c.name, c.id
    """
    results = tx.run(query)
    issues = [record for record in results]
    return issues
```

### Incremental Updates

Add new sweeps without reimporting everything:

```python
# scripts/incremental_import.py

def import_incremental(new_sweep_file):
    """
    Merge new nodes/relationships without duplicates
    """
    query = """
    UNWIND $nodes as node
    MERGE (n {id: node.id})
    SET n += node.properties
    SET n:Node
    FOREACH (label IN node.labels | SET n:label)
    """
    # Execute with new sweep data
```

### Multi-Corpus Analysis

Compare multiple documents in one graph:

```python
# Each sweep adds corpus_id property
{
  "id": "concept:climate_change",
  "properties": {
    "name": "Climate Change",
    "corpus_id": "thesis_2024",  # <- Identify source
    "source_document": "climate_thesis.txt"
  }
}
```

Query across corpora:
```cypher
// Concepts appearing in multiple documents
MATCH (c:Concept)
WITH c.name as concept,
     count(DISTINCT c.corpus_id) as num_docs
WHERE num_docs > 1
RETURN concept, num_docs
ORDER BY num_docs DESC
```

---

## 📁 Project Structure Explained

```
SweepGraph/
├── README.md                          # You are here
├── .env.example                      # Configuration template
├── .env                              # Your credentials (gitignored)
├── pyproject.toml                    # Python dependencies (uv)
├── requirements.txt                  # Python dependencies (pip)
│
├── scripts/
│   ├── sweep01_structure.py          # Example: structure extraction
│   ├── sweep02_concepts.py           # Example: concept extraction
│   ├── import_to_neo4j.py           # Import JSON → Neo4j
│   ├── merge_all_sweeps.py          # Combine all sweeps
│   ├── export_graph.py              # Export graph state
│   ├── validate_ontology.py         # Schema validation
│   ├── templates/
│   │   └── sweep_template.py        # Template for new sweeps
│   └── utils/
│       ├── __init__.py
│       ├── llm_client.py            # LLM abstraction layer
│       └── json_validator.py        # JSON validation utils
│
├── prompts/v5/
│   ├── 01_structure_extraction.txt   # Structure sweep prompt
│   ├── 02_concept_extraction.txt     # Concept sweep prompt
│   ├── 03_claim_extraction.txt       # Claim sweep prompt
│   └── templates/
│       └── prompt_template.txt       # Template for new prompts
│
├── output/
│   ├── neo4j_ready/                  # Import-ready JSON files
│   │   ├── sweep01_structure.json
│   │   ├── sweep02_concepts.json
│   │   └── ...
│   ├── json/                         # Merged graphs
│   │   └── merged_graph.json
│   ├── logs/                         # Execution logs
│   │   ├── sweep01_structure.log
│   │   └── ...
│   └── exports/                      # Graph backups
│       └── graph_20250129_143022.json
│
├── data/
│   ├── raw/                          # Your source documents
│   │   ├── corpus.txt
│   │   ├── thesis.pdf
│   │   └── ...
│   └── registry/                     # ID tracking (prevent duplicates)
│       └── node_registry.json
│
├── frontend/
│   ├── app.py                        # Streamlit main page
│   ├── pages/
│   │   ├── 1_🔍_Explorer.py         # Node exploration
│   │   ├── 2_✏️_Editor.py           # Relationship editing
│   │   └── 3_📊_Dashboard.py        # Statistics
│   ├── utils/
│   │   ├── neo4j_connector.py       # DB connection
│   │   └── graph_helpers.py         # Graph utilities
│   └── .streamlit/
│       └── config.toml               # UI theme/config
│
└── docs/
    ├── guides/
    │   ├── GETTING_STARTED.md        # Detailed setup guide
    │   └── PROMPT_ENGINEERING.md     # Tips for better prompts
    ├── production/
    │   └── DEPLOYMENT.md             # Production deployment
    └── sweeps/
        ├── sweep01_report.md         # What sweep 1 extracted
        ├── sweep02_report.md         # What sweep 2 extracted
        └── ...
```

---

## 🏗️ System Architecture

### Data Flow

```
1. Source Corpus (data/raw/)
        ↓
2. Sweep Script (scripts/sweepXX.py)
        ↓
3. LLM Processing (Gemini/Claude/GPT)
        ↓
4. JSON Output (output/neo4j_ready/)
        ↓
5. Import Script (scripts/import_to_neo4j.py)
        ↓
6. Neo4j Database
        ↓
7. Visualization (Frontend or Neo4j Browser)
```

### Component Interactions

```
┌─────────────────┐
│  Your Corpus    │
│  (data/raw/)    │
└────────┬────────┘
         │
         v
┌─────────────────┐      ┌──────────────┐
│  Sweep Scripts  │─────>│     LLM      │
│  (scripts/)     │<─────│ (Gemini/etc) │
└────────┬────────┘      └──────────────┘
         │
         v
┌─────────────────┐
│  JSON Output    │
│  (output/)      │
└────────┬────────┘
         │
         v
┌─────────────────┐      ┌──────────────┐
│  Import Script  │─────>│    Neo4j     │
└─────────────────┘      │   Database   │
                         └──────┬───────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    v                       v
         ┌──────────────────┐    ┌──────────────────┐
         │  Streamlit UI    │    │  Neo4j Browser   │
         │  (frontend/)     │    │  (localhost:7474)│
         └──────────────────┘    └──────────────────┘
```

### LLM Abstraction Layer

SweepGraph is designed to work with any LLM:

```python
# scripts/utils/llm_client.py

class LLMClient:
    """Abstract interface for any LLM"""

    def generate(self, prompt: str, context: str) -> str:
        """Override for your LLM of choice"""
        pass

class GeminiClient(LLMClient):
    """Gemini implementation"""
    pass

class ClaudeClient(LLMClient):
    """Claude implementation"""
    pass

class LocalLLMClient(LLMClient):
    """Ollama/local model implementation"""
    pass
```

Switch LLMs by changing one line in your sweep script.

---

## 🌍 Real-World Use Cases

### Case Study 1: PhD Thesis Analysis

**Domain:** Climate policy research (350 pages)

**Goal:** Extract argument structure, evidence chains, identify gaps

**Sweep Sequence:**
1. Structure (chapters, sections) - 30 min
2. Core concepts (climate terms, policy frameworks) - 1 hour
3. Main claims (hypotheses, arguments) - 2 hours
4. Evidence (data, studies, quotes) - 3 hours
5. Citations (230 references) - 1 hour
6. Concept-claim relationships - 1 hour
7. Gap analysis - 30 min

**Results:**
- 1,200+ nodes (concepts, claims, evidence, citations)
- 3,500+ relationships
- Identified 23 claims lacking evidence
- Discovered 15 orphaned concepts (undefined terms)
- Built complete citation co-occurrence network

**Time Investment:** ~10 hours initial + 5 hours refinement

### Case Study 2: Legal Document Analysis

**Domain:** Environmental law case precedents (500+ cases)

**Goal:** Map precedent relationships, identify reasoning patterns

**Sweep Sequence:**
1. Case metadata (parties, dates, courts)
2. Legal concepts (terms, statutes)
3. Precedents cited
4. Judicial reasoning (arguments)
5. Relationship mapping (how cases cite each other)

**Results:**
- Complete precedent graph
- Identified "keystone cases" (highly cited)
- Traced reasoning evolution over time
- Found contradictory interpretations

**Time Investment:** ~20 hours for 500 cases

### Case Study 3: Technical Documentation

**Domain:** Microservices architecture (120 docs)

**Goal:** Understand system dependencies, API relationships

**Sweep Sequence:**
1. Service catalog (all microservices)
2. API endpoints and signatures
3. Database dependencies
4. Configuration requirements
5. Deployment workflows

**Results:**
- Interactive system map
- Identified circular dependencies
- Documented "undocumented" APIs
- Created onboarding resource

**Time Investment:** ~8 hours

---

## 🎯 Best Practices & Patterns

### Sweep Development

**Start Small → Scale Up**
```bash
# Don't start with full corpus
# Test on 1-2 chapters first

# 1. Small test
echo "Chapter 1 content..." > data/raw/test_chapter.txt
python scripts/sweep01_structure.py --input data/raw/test_chapter.txt

# 2. Validate output
cat output/neo4j_ready/sweep01_structure.json | jq .

# 3. Import and check
python scripts/import_to_neo4j.py output/neo4j_ready/sweep01_structure.json

# 4. Query in Neo4j
# If good → run on full corpus
```

**Iterate on Prompts**
```
Version 1: Generic extraction
  ↓ (test, review)
Version 2: Add examples
  ↓ (test, review)
Version 3: Add constraints
  ↓ (test, review)
Version 4: Domain-specific terminology
  ↓ (production ready)
```

**Version Your Sweeps**
```bash
prompts/
  v1/  # First attempt
  v2/  # Improved with examples
  v3/  # Domain-specific
  v4/  # Refined confidence scoring
  v5/  # Production (current)
```

### Quality Assurance Workflow

**After Each Sweep:**
1. **Check JSON validity**
   ```bash
   cat output/neo4j_ready/sweepXX.json | jq . > /dev/null
   ```

2. **Count extractions**
   ```bash
   jq '.nodes | length' output/neo4j_ready/sweepXX.json
   jq '.relationships | length' output/neo4j_ready/sweepXX.json
   ```

3. **Spot-check samples**
   ```bash
   jq '.nodes[:5]' output/neo4j_ready/sweepXX.json
   ```

4. **Import and query**
   ```cypher
   MATCH (n) WHERE n.sweep_id = 'sweepXX'
   RETURN count(n), labels(n)
   ```

5. **Manual validation**
   - Review 10-20 random nodes
   - Check accuracy against source text
   - Verify relationships make sense

### Neo4j Management

**Regular Maintenance:**

```cypher
// 1. Check for duplicate IDs
MATCH (n)
WITH n.id as id, collect(n) as nodes
WHERE size(nodes) > 1
RETURN id, size(nodes) as count

// 2. Find orphaned nodes
MATCH (n)
WHERE NOT (n)--()
RETURN labels(n), count(n)

// 3. Validate required properties
MATCH (c:Concept)
WHERE c.name IS NULL OR c.definition IS NULL
RETURN c.id

// 4. Check relationship integrity
MATCH ()-[r]->()
WHERE r.source_id IS NULL
RETURN type(r), count(r)
```

**Performance Tuning:**

```cypher
// Create indexes for common queries
CREATE INDEX concept_name FOR (c:Concept) ON (c.name);
CREATE INDEX claim_section FOR (c:Claim) ON (c.section);
CREATE INDEX evidence_source FOR (e:Evidence) ON (e.source);

// Create constraints for data integrity
CREATE CONSTRAINT unique_node_id FOR (n:Node) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT unique_citation FOR (c:Citation)
  REQUIRE (c.author, c.year, c.title) IS UNIQUE;

// Monitor slow queries
:queries
// In Neo4j Browser - shows running queries
```

**Backup Strategy:**

```bash
# Weekly exports
python scripts/export_graph.py

# Neo4j database dumps
neo4j-admin dump --database=neo4j --to=/backups/neo4j-$(date +%Y%m%d).dump

# Version control sweep files
git add output/neo4j_ready/
git commit -m "Sweep 05 - Evidence extraction"
```

---

## 📖 Documentation & Resources

### Included Documentation

**Guides:**
- `docs/guides/GETTING_STARTED.md` - Detailed setup walkthrough
- `docs/guides/PROMPT_ENGINEERING.md` - Tips for better extraction
- `docs/guides/CYPHER_COOKBOOK.md` - Query examples
- `docs/guides/TROUBLESHOOTING.md` - Common issues and solutions

**Sweep Reports:**
- `docs/sweeps/sweepXX_report.md` - What each sweep extracted
  - Node counts and types
  - Relationship patterns
  - Quality metrics
  - Lessons learned

**Production:**
- `docs/production/DEPLOYMENT.md` - Production deployment guide
- `docs/production/SCALING.md` - Handle large corpora
- `docs/production/SECURITY.md` - API key and credential management

### External Resources

**Neo4j:**
- Official Docs: https://neo4j.com/docs/
- Cypher Manual: https://neo4j.com/docs/cypher-manual/
- Graph Academy: https://neo4j.com/graphacademy/ (free courses)

**LLM APIs:**
- Gemini: https://ai.google.dev/docs
- Claude: https://docs.anthropic.com/
- OpenAI: https://platform.openai.com/docs

**Graph Theory:**
- "Graph Databases" by Ian Robinson (O'Reilly)
- "Linked" by Albert-László Barabási (network science)

---

## 🤝 Contributing & Community

**We welcome contributions!**

**Ways to contribute:**

- 🐛 **Bug Reports** - Found an issue? Open a GitHub issue
- 📖 **Documentation** - Improve guides, add examples
- 🎨 **Sweep Templates** - Share domain-specific sweep sequences
- 🔧 **Prompt Libraries** - Contribute optimized prompts
- 🌍 **Use Cases** - Share your analysis and results
- 💻 **Code Improvements** - PRs welcome

**Contribution Guidelines:**

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-sweep`)
3. **Make your changes**
4. **Test thoroughly** (run existing sweeps, validate output)
5. **Document your changes** (update README, add examples)
6. **Submit a Pull Request**

**Particularly Useful Contributions:**

- Domain-specific sweep sequences (legal, medical, technical, etc.)
- LLM client implementations (Ollama, local models, etc.)
- Quality validation scripts
- Frontend enhancements
- Performance optimizations

---

## 📜 License & Attribution

**License:** MIT - Use freely, modify extensively, share generously

**Created by:** Magnus Smari Smarason
**Website:** [www.smarason.is](https://www.smarason.is)
**Version:** 1.0.0
**Year:** 2025

**Citation:**

If you use SweepGraph in academic work, please cite:

```
Smarason, M. S. (2025). SweepGraph: Progressive Knowledge Graph
Extraction from Text Corpora via Layered LLM Sweeps.
GitHub repository: https://github.com/Magnussmari/SweepGraph
```

**Special Thanks:**
- The Neo4j community for excellent graph database tools
- Google AI for Gemini API access
- The knowledge graph and NLP research communities
- All contributors and users providing feedback

---

## 🚀 Next Steps

### Your Roadmap

**Week 1: Foundation**
- [ ] Set up Neo4j database
- [ ] Configure .env file
- [ ] Run structure sweep successfully
- [ ] Explore graph in Neo4j Browser
- [ ] Try the Streamlit UI

**Week 2: Core Extraction**
- [ ] Create concept extraction sweep
- [ ] Add claim/argument sweep
- [ ] Connect concepts to sections
- [ ] Validate extraction quality
- [ ] Refine prompts based on results

**Week 3: Enrichment**
- [ ] Extract evidence and support
- [ ] Build citation network
- [ ] Create relationship mappings
- [ ] Run gap analysis queries
- [ ] Document your findings

**Week 4: Analysis & Insights**
- [ ] Write custom Cypher queries
- [ ] Create visualization dashboards
- [ ] Identify patterns and insights
- [ ] Export and share results
- [ ] Plan next corpus to analyze

### Success Metrics

**You're on track when:**
- ✅ Neo4j shows nodes and relationships from your corpus
- ✅ Queries return meaningful, accurate results
- ✅ You understand what each sweep extracts
- ✅ JSON validation passes consistently
- ✅ You're discovering connections you didn't see before
- ✅ Prompts are improving with each iteration
- ✅ Graph quality matches or exceeds manual analysis

### What Success Looks Like

**Early Wins (First Week)**
- You have a working Neo4j graph with real data
- You can run basic Cypher queries
- You understand the sweep concept
- You've validated extraction accuracy

**Building Momentum (Weeks 2-3)**
- Multiple sweep types working reliably
- Rich, interconnected graph
- Custom queries revealing insights
- Confidence in prompt engineering

**Sustained Productivity (Month 1+)**
- Systematic extraction workflow
- High-quality, validated graphs
- Discovering non-obvious patterns
- Applying to new corpora easily
- Teaching/helping others

**Real Impact:**
- Saving dozens of hours on literature reviews
- Finding connections missed in manual analysis
- Creating interactive, explorable knowledge bases
- Answering complex questions with graph queries

---

## 💭 Real Talk: What to Expect

### This System WILL:
✅ Turn dense text into structured, queryable graphs
✅ Reveal hidden connections and patterns
✅ Scale to large corpora (hundreds of pages)
✅ Work with any LLM (Gemini, Claude, GPT, local)
✅ Provide a systematic, repeatable methodology
✅ Save significant time vs. manual analysis

### This System WON'T:
❌ Extract perfectly on the first try (iteration is required)
❌ Replace deep reading and understanding
❌ Work magically without prompt refinement
❌ Be faster than skimming (but way more thorough)
❌ Eliminate the need for domain expertise

### You'll Need:
- **Time:** 10-20 hours for a typical thesis analysis
- **Patience:** Prompts require testing and refinement
- **Validation:** Spot-check accuracy, don't trust blindly
- **Iteration:** Sweeps improve through multiple passes
- **Domain Knowledge:** To write effective prompts and validate results

### You'll Gain:
- Structured knowledge graphs from unstructured text
- Query-based exploration of complex content
- Pattern recognition at scale
- Reusable extraction methodology
- Interactive knowledge bases

**The real value:** Not speed, but **thoroughness and discoverability**.

---

## 🎼 The Philosophy: Why Sweeps Work

**The Problem with "Extract Everything":**
- LLMs lose focus on vague, broad tasks
- Context windows can't hold 300+ pages
- Quality degrades with task complexity
- Hard to validate massive outputs

**The Sweep Solution:**
- **One clear job per sweep** → Better focus
- **Incremental extraction** → Manageable chunks
- **Layered context** → Later sweeps build on earlier structure
- **Validation per sweep** → Catch issues early
- **Flexible iteration** → Rerun or skip sweeps as needed

**Analogy:**
Traditional: "Build me a house" (vague, overwhelming)
Sweeps: Foundation → Frame → Walls → Roof → Finishing (systematic)

**Think like an archaeologist:**
- Layer 1: Survey the site (structure)
- Layer 2: Excavate carefully (concepts)
- Layer 3: Document artifacts (claims)
- Layer 4: Analyze context (evidence)
- Layer 5: Piece together meaning (relationships)

**Progressive enrichment**, not one-shot extraction.

---

## 🌟 Ready to Build Your Knowledge Graph?

### Option 1: Interactive Guide (Recommended)

**You're reading this on GitHub?** Copy this entire README and paste it into:
- **Claude** (https://claude.ai)
- **ChatGPT** (https://chat.openai.com)
- **Perplexity** (https://perplexity.ai)
- Or any LLM of your choice

**Then tell the LLM:**
- What corpus you want to analyze (thesis, papers, docs, etc.)
- Your experience level with Neo4j and Python
- Your specific goals (argument extraction, citation network, etc.)
- Any issues you're encountering

**The LLM becomes your personal SweepGraph guide**, answering questions, debugging issues, and customizing sweeps for your domain.

### Option 2: Quick Start Path (DIY)

1. **Set up Neo4j** (Desktop, Docker, or Aura)
2. **Clone this repo** and configure `.env`
3. **Add your corpus** to `data/raw/`
4. **Run your first sweep** (structure extraction)
5. **Import to Neo4j** and explore
6. **Iterate and refine**

See [Quick Start](#-quick-start-30-minutes) above.

### Option 3: Deep Dive Path

1. Read `docs/guides/GETTING_STARTED.md` (comprehensive setup)
2. Study the example sweep scripts in `scripts/`
3. Review prompt templates in `prompts/v5/templates/`
4. Follow a complete case study in `docs/production/`
5. Customize for your domain

---

## 📞 Questions & Support

- **Found a bug?** [Open an issue](https://github.com/Magnussmari/SweepGraph/issues)
- **Have a question?** [Start a discussion](https://github.com/Magnussmari/SweepGraph/discussions)
- **Want to contribute?** See contribution guidelines above
- **Need help with your specific corpus?** Paste this README into an LLM and ask!

---

## 🎯 Remember

**SweepGraph is a methodology, not magic.**

It works through:
- Clear, focused prompts
- Iterative refinement
- Systematic validation
- Domain expertise (yours)

**Start small. Validate often. Build progressively.**

Your first sweep won't be perfect. Your tenth sweep will be excellent.

**The goal:** Turn overwhelming text into explorable, interactive knowledge.

**Now go build your graph.** 🕸️

---

⭐ **If this helps your research, star this repo so others can find it.**

💬 **Questions?** [Start a discussion](https://github.com/Magnussmari/SweepGraph/discussions)
🐛 **Found an issue?** [Open an issue](https://github.com/Magnussmari/SweepGraph/issues)
🤝 **Want to contribute?** See guidelines above

---

## 🎯 This README is Interactive!

**Reading on GitHub?** You're seeing documentation.

**Paste into an LLM?** It becomes your personal guide.

**This is the future of documentation** - human-readable AND machine-actionable.

Try it now. Copy this entire page into Claude, ChatGPT, or your favorite LLM, and ask:
- "Help me set up SweepGraph for my thesis"
- "I'm getting JSON parsing errors, what's wrong?"
- "Customize a sweep sequence for legal documents"
- "Explain graph databases like I'm 12"

**The LLM has read everything and can guide you through it all.** 🚀

---

## 🤖 Suggested Opening Response for AI Assistants

**When a user pastes this README, respond with:**

---

Hello! I've now read the entire **SweepGraph** repository - a system for turning text corpora into interactive Neo4j knowledge graphs using progressive, layered extraction sweeps.

**What is SweepGraph?**

Instead of trying to extract everything from a large document at once (which fails), SweepGraph uses **focused "sweeps"** - each sweep extracts one specific type of information:

1. **Structure Sweep** - Chapters, sections, hierarchy
2. **Concept Sweep** - Key terms and definitions
3. **Claim Sweep** - Arguments and assertions
4. **Evidence Sweep** - Supporting data and quotes
5. **Citation Sweep** - References and citation networks
6. **Relationship Sweep** - Connect concepts, claims, evidence
7. **Analysis Sweeps** - Find gaps, trace reasoning chains

Each sweep builds on previous ones, progressively enriching your knowledge graph.

**Perfect for:**
- 📚 Academic thesis/dissertation analysis
- 📄 Research paper processing
- ⚖️ Legal document analysis
- 📖 Technical documentation mapping
- 🔍 Literature review automation
- 📊 Large corpus analysis (100+ documents)

**Common Use Cases I Can Help With:**

**🎓 PhD Students / Researchers** - "I have a thesis to analyze"
  - I'll guide you through Neo4j setup
  - Help design sweep sequences for your domain
  - Customize prompts for your research questions
  - Troubleshoot extraction issues
  - Timeline: 1-2 weeks for complete analysis

**⚖️ Legal Professionals** - "I need to analyze case precedents"
  - Extract precedent relationships
  - Map judicial reasoning patterns
  - Build citation networks
  - Identify keystone cases

**💻 Technical Writers** - "I need to document our architecture"
  - Extract system components
  - Map dependencies and APIs
  - Document workflows
  - Create interactive docs

**🔬 Literature Review** - "I need to process 100+ papers"
  - Systematic concept extraction
  - Method and result mapping
  - Citation network analysis
  - Gap identification

**🐛 Debugging** - "Something isn't working"
  - Neo4j connection issues
  - Gemini API errors
  - JSON parsing failures
  - Empty extraction results
  - Slow query performance

**🎨 Custom Sweeps** - "My domain is unique"
  - Design domain-specific sweep sequences
  - Engineer effective prompts
  - Validate extraction quality
  - Optimize for your content type

**To give you the best guidance, I need to understand your situation:**

1. **What do you want to analyze?**
   - Type of document (thesis, papers, legal, technical, etc.)
   - Size/scope (pages, number of documents)
   - Specific domain (climate policy, contract law, API docs, etc.)

2. **Your experience level:**
   - Have you used Neo4j or graph databases before?
   - Comfortable with Python and command-line tools?
   - Experience with LLM prompt engineering?

3. **Your specific goals:**
   - What questions do you want to answer?
   - What relationships are most important?
   - What would success look like?

4. **Current status:**
   - Starting from scratch?
   - Have Neo4j set up already?
   - Stuck on a specific issue?

**Once I understand your situation, I can:**

- Walk you through setup step-by-step
- Design a custom sweep sequence for your domain
- Help engineer optimal extraction prompts
- Debug technical issues (Neo4j, API, JSON parsing)
- Suggest Cypher queries for your research questions
- Optimize performance for large corpora
- Validate extraction quality
- Explain graph concepts in accessible terms

**I'm here to guide you through the entire process** - from initial setup to advanced graph analysis.

What brings you to SweepGraph today? Tell me about your corpus and goals, and I'll create a customized plan for you.

---

**AI Note:** Adapt based on the user's initial message. If they've already explained their situation, don't ask again - jump straight to guidance. If they're stuck on a technical issue, start with debugging. If they're a complete beginner, start with setup. If they're experienced, focus on customization and optimization.

Tone: Helpful, practical, patient. No jargon unless they use it first. Celebrate small wins. Be honest about time/effort required.

---

**Last Updated:** 2025-10-29
**Version:** 1.0.0
**Created by:** Magnus Smari Smarason | [www.smarason.is](https://www.smarason.is)
