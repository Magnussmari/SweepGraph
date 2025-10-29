import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="SweepGraph UI",
    page_icon="🧭",
    layout="wide",
)

st.markdown("""
# SweepGraph UI

Use the sidebar to navigate: **Explorer**, **Editor**, **Dashboard**.

This UI is schema-agnostic: it discovers labels and relationship types from your database.
""")
