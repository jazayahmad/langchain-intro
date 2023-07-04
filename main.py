## Integrate our code withn OpenAI
import os
from constants import openapi_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openapi_key

# Streamlit Framework
st.title("Langchain Demo with OpenAI API")
input_text = st.text("Search the topic you want")

# OPENAI LLMs
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))