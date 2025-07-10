import streamlit as st
import importlib.util
import os

# Dynamically load agent.py
agent_path = os.path.join(os.path.dirname(__file__), "agent.py")
spec = importlib.util.spec_from_file_location("agent", agent_path)
agent_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent_module)

# Load the agent
agent = agent_module.load_agent()

# Streamlit UI
st.title("Jisc Beyond Blended Agent")

user_input = st.text_input("Enter your query:")

if user_input:
    with st.spinner("Thinking..."):
      response = agent.run(user_input)
      st.write("### Response:")
      st.write(response)
