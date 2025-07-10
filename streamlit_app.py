
import streamlit as st
import sys
import os

# Ensure the current directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the agent loader
from agent import load_agent

# Load the agent
agent = load_agent()

# Streamlit UI
st.title("Jisc Beyond Blended Agent")

user_input = st.text_input("Enter your query:")

if user_input:
  with st.spinner("Thinking..."):
      response = agent.run(user_input)
        st.write("### Response:")
        st.write(response)
