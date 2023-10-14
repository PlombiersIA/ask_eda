import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/cmarkea/bloomz-560m-sft-chat"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Prompt the user for input
prompt = st.text_input("Enter your prompt here:")

# Send the input to the API and display the response
if prompt:
    response = query({"inputs": prompt})
    st.write(response["generated_text"])