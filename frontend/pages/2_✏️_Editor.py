import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import streamlit as st

from frontend.utils.graph_helpers import flatten_node_for_display, search_nodes
from frontend.utils.neo4j_connector import get_labels, run_cypher

st.title("✏️ Editor (Relationships)")

st.subheader("Find nodes")

label_options = ["<any>"] + get_labels()

lookup_cols = st.columns(3)
with lookup_cols[0]:
    lookup_label = st.selectbox("Label", label_options, help="Restrict results to a node label")
with lookup_cols[1]:
    lookup_prop_key = st.text_input("Property key", placeholder="name", help="Leave blank to search all properties")
with lookup_cols[2]:
    lookup_limit = st.slider("Limit", 5, 200, 50, 5, key="lookup_limit")

lookup_term = st.text_input("Contains", placeholder="Type to filter node properties", key="lookup_term")

lookup_nodes = search_nodes(
    label=None if lookup_label == "<any>" else lookup_label,
    term=lookup_term or None,
    property_key=lookup_prop_key or None,
    limit=lookup_limit,
)

lookup_records = [flatten_node_for_display(node) for node in lookup_nodes]

if lookup_records:
    lookup_df = pd.DataFrame(lookup_records)
    preferred = [col for col in ["labels", "name", "title", "id", "element_id"] if col in lookup_df.columns]
    remainder = [col for col in lookup_df.columns if col not in preferred]
    ordered_lookup_df = lookup_df[preferred + remainder] if preferred or remainder else lookup_df
    st.caption(f"Found {len(ordered_lookup_df)} matching nodes")
    st.dataframe(ordered_lookup_df, use_container_width=True, hide_index=True)
else:
    st.info("No nodes match the current search.")

st.divider()

with st.form("create_rel"):
    st.subheader("Create relationship")
    source_id = st.text_input("Source node id (property id)")
    target_id = st.text_input("Target node id (property id)")
    rel_type = st.text_input("Relationship type", value="RELATED_TO")
    submitted = st.form_submit_button("Create")
    if submitted and source_id and target_id and rel_type:
        q = f"""
        MATCH (a {{id: $source}})
        MATCH (b {{id: $target}})
        MERGE (a)-[r:{rel_type}]->(b)
        RETURN type(r) AS created
        """
        res = run_cypher(q, {"source": source_id, "target": target_id})
        if res:
            st.success(f"Created relationship of type {res[0].get('created')}")
        else:
            st.warning("The database did not report a created relationship.")

with st.form("delete_rel"):
    st.subheader("Delete relationship")
    source_id_d = st.text_input("Source id")
    target_id_d = st.text_input("Target id")
    rel_type_d = st.text_input("Type", value="RELATED_TO")
    del_submit = st.form_submit_button("Delete")
    if del_submit and source_id_d and target_id_d and rel_type_d:
        q = f"""
        MATCH (a {{id: $source}})-[r:{rel_type_d}]->(b {{id: $target}})
        DELETE r
        RETURN 1 AS deleted
        """
        res = run_cypher(q, {"source": source_id_d, "target": target_id_d})
        if res:
            st.success("Relationship deleted")
        else:
            st.info("No matching relationship found to delete.")
