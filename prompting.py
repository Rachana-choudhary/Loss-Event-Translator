import os
import openai
import toml
import streamlit as st

#secrets = toml.load("secrets.toml")
#openai.api_key = secrets["openai_api_key"]

openai.api_key = st.secrets["openai_api_key"]


def generate_risks(risk_description):
    text = f"""Rewrite the following text "{risk_description}"  by correcting the grammatical errors
     Please take some time to think and then provide only a complete rewritten text , I don't need any explanation."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.6,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
