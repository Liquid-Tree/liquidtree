import streamlit as st
from openai import OpenAI


print(completion.choices[0].message)
st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  temperature=0.7,
)
print()
# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

