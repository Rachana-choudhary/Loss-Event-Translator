import streamlit as st
import json
import pandas as pd
import prompting
from PIL import Image
import streamlit.components.v1 as components

im = Image.open("./assets/images/RS-square-logo.jpeg")

st.set_page_config(
    layout="wide", page_title="RiskSpotlight - Loss Event Translator", page_icon=im
)

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
                # img {position: absolute; top: 0; left: 0;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Loss Event Translator")

col1, col2 = st.columns(2)

with col1:
    loss_event = st.text_area("Please provide loss event description...", value="", height=200)
    clicked = st.button("Submit")

with col2:
    languages = st.multiselect(
        "Languages",
        ["English", 
        "French",
        "German",
        "Spanish",
        "Itanlian",
        "Chinese",
        "Arabic",
        "Greek"],
    )

if clicked:
    if not loss_event or not languages:
        st.warning("Please fill in all the information.")

    else:
        with st.spinner("Please wait..."):
            response = prompting.generate_description(loss_event, languages)

            loss_event_output = response["choices"][0]["message"]["content"]       
            st.write(loss_event_output)    
