import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from frontend.utils.neo4j_connector import run_cypher

st.title("📊 Dashboard")

node_count = run_cypher("MATCH (n) RETURN count(n) AS c")[0]["c"]
rel_count = run_cypher("MATCH ()-[r]->() RETURN count(r) AS c")[0]["c"]

col1, col2 = st.columns(2)
col1.metric("Nodes", node_count)
col2.metric("Relationships", rel_count)

st.subheader("Top relationship types")
rows = run_cypher("""
    MATCH ()-[r]->()
    RETURN type(r) AS type, count(*) AS c
    ORDER BY c DESC
    LIMIT 10
""")
st.dataframe(rows)
