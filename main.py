import sys
import os

# Add the directory containing agent.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from agent import load_agent

st.title("Jisc Beyond Blended Agent")
query = st.text_input("Ask me anything about Beyond Blended:")

if query:
    agent = load_agent()
    response = agent.run(query)
    st.write(response)
