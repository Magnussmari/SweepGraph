import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import streamlit as st

from frontend.utils.graph_helpers import flatten_node_for_display, search_nodes
from frontend.utils.neo4j_connector import get_labels, get_relationship_types

st.title("🔍 Explorer")

labels = get_labels()
rel_types = get_relationship_types()

filters = st.columns(3)
with filters[0]:
    sel_label = st.selectbox("Label", ["<any>"] + labels)
with filters[1]:
    sel_rel = st.selectbox("Relationship", ["<any>"] + rel_types)
with filters[2]:
    prop_key = st.text_input("Property key", placeholder="name", help="Optional property to target in search")

search_term = st.text_input("Contains", placeholder="Search across node properties")
limit = st.slider("Limit", 10, 500, 100, 10)

nodes = search_nodes(
    label=None if sel_label == "<any>" else sel_label,
    relationship_type=None if sel_rel == "<any>" else sel_rel,
    term=search_term or None,
    property_key=prop_key or None,
    limit=limit,
)

records = [flatten_node_for_display(node) for node in nodes]

if records:
    df = pd.DataFrame(records)
    preferred = [col for col in ["labels", "name", "title", "id", "element_id"] if col in df.columns]
    remainder = [col for col in df.columns if col not in preferred]
    ordered_df = df[preferred + remainder] if preferred or remainder else df
    st.caption(f"Showing {len(ordered_df)} nodes")
    st.dataframe(ordered_df, use_container_width=True, hide_index=True)
else:
    st.info("No nodes matched your filters.")
