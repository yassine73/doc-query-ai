"""Main entry point for the Streamlit application."""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="RAG Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function."""
    st.title("🤖 RAG Agent")
    st.write("Welcome to the RAG Agent application!")
    
    # Add your main application code here

if __name__ == "__main__":
    main()
