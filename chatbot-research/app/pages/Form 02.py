import base64
import streamlit as st

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown("# CARE Policy and Waiver for In Person or In Clinic Service for COVID-19 and COVID Variants 1.21")
st.sidebar.markdown("# CARE Policy and Waiver for In Person or In Clinic Service for COVID-19 and COVID Variants 1.21")

show_pdf('./data/forms/CARE Policy and Waiver for In Person or In Clinic Service for COVID-19 and COVID Variants 1.21.pdf')