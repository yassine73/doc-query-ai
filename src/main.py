from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from groq import Groq

client = Groq()
def generate_response(query: str):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama-3.1-8b-instant",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=True,
    )

    for chunk in stream:
        chunk_content = chunk.choices[0].delta.content
        yield chunk_content if chunk_content is not None else ""

def chat_interface():
    new_chat = st.sidebar.button("New Chat", type="primary")
    if "messages" not in st.session_state or new_chat:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if query := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.write(query)

        st.session_state.messages.append({"role": "user", "content": query})

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response(query))
        st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    chat_interface()


if __name__ == "__main__":
    main()