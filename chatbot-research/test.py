# import streamlit as st
# import base64

# def show_pdf(file_path):
#     with open(file_path,"rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

# show_pdf('./data/forms/Representations and Warranties - Client Over 18 11.21.pdf')

# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Contents of ~/my_app/pages/page_2.py
import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

# Contents of ~/my_app/pages/page_3.py
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
