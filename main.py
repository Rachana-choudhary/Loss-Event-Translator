import streamlit as st
import prompting
from PIL import Image
import streamlit.components.v1 as components

im = Image.open("./assets/images/RS-square-logo.jpeg")

st.set_page_config(
    layout="wide", page_title="RiskSpotlight - OpRisk Risk Guidance", page_icon=im
)

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("OpRisk Risk Guidance")

risk_description = st.text_area("Please provide Risk Description.", value="", height=120)
clicked = st.button("Submit")


if clicked:
    if not risk_description:
        st.warning("Please fill in all the information.")

    else:
        with st.spinner("Please wait..."):
            response = prompting.generate_risks(risk_description)


            risks_output = response["choices"][0]["message"]["content"]
            st.write(risks_output)