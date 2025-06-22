import streamlit as st
import openai

# Set up the page
st.title("Conscious AI Agent")
st.write("An AI agent designed to be logical and empathetic")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response (your existing function here)
    with st.chat_message("assistant"):
        response = your_existing_chatgpt_function(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})