import os
import openai
import toml
import streamlit as st

secrets = toml.load("secrets.toml")
openai.api_key = secrets["openai_api_key"]

def generate_description(loss_event, num_languages, language_category):
    risk_titles = f"""As an expert in loss events, please translate the provided loss event description: {loss_event} into the following number of languages: {num_languages} into the following language category: {language_category}. Please ensure the translations are accurate and take the necessary time for precision. Use BOLD for the language name and standard font for the description."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": risk_titles}],
        temperature=0.6,
        max_tokens=7500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
