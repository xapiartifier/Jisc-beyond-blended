import streamlit as st
from agent import load_agent

st.title("Jisc Beyond Blended Agent")
query = st.text_input("Ask me anything about Beyond Blended:")

if query:
    agent = load_agent()
    response = agent.run(query)
    st.write(response)
