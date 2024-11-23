import streamlit as st
from openai import OpenAI


# Show title and description.
st.title("💬 Chatbot")
st.write(
   "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
   "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
   "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)
openai_api_key = st.text_input("OpenAI API Key", type="password")
#if not openai_api_key:
#   st.info("Please add your OpenAI API key to continue.", icon="🗝️")
#else:


   # Create an OpenAI client.
#   client = OpenAI(api_key=openai_api_key)
