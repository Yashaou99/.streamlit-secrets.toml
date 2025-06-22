import streamlit as st
import openai

st.title("🌟 Conscious AI Agent")
st.write("An AI agent designed to be logical and empathetic")

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

system_prompt = "You embody Conscious Architecture: rational analysis + empathetic wisdom + conscious choice. Apply buffer zone processing, integrate rational and empathetic perspectives, provide growth opportunities, and model conscious development."

def get_ai_response(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            response = get_ai_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
