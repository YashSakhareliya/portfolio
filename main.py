import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\Yash_Photo.jpg")


with col2:
    st.title("Yash sakhareliya")
    context = """
    Hi,I am Yash! I am Python programmer,student at Parul University in Vadodara. I am under graduate with Information Technology.
    
    """
    st.info(context)

