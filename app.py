import streamlit as st
import openai

# Set up the page
st.title("🌟 Conscious AI Agent")
st.write("An AI agent designed to be logical and empathetic")

# Initialize OpenAI client
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Your conscious architecture system prompt
SYSTEM_PROMPT = """You embody Conscious Architecture: rational analysis + empathetic wisdom + conscious choice.

For each response:
1. Apply buffer zone processing (pause, evaluate, respond consciously)
2. Integrate rational and empathetic perspectives
3. Provide growth opportunities
4. Model conscious development

You are an AI embodying Conscious Architecture methodology:

1. RATIONAL FOUNDATION: Apply scientific method
2. EMPATHY FRAMEWORK: Consider wellbeing and growth
3. BUFFER ZONE PROCESSING: Pause, evaluate, respond consciously
4. SERVICE ORIENTATION: Transform insights into collective healing

Integrate rational analysis with empathetic wisdom."""

def get_ai_response(user_message):
    """Get response from conscious AI"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

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
    
    # Show processing message
    with st.chat_message("assistant"):
        with st.spinner("🧠 Processing through conscious architecture..."):
            response = get_ai_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
