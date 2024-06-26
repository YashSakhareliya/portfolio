import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\Yash_Photo.jpg", width=400)


with col2:
    st.title("Yash sakhareliya")
    context = """
    Hi,I am Yash! I am Python programmer,student at Parul University in Vadodara. I am under graduate with Information Technology.
    
    """
    st.info(context)


context2 = """
This is project description 
"""
st.write(context2)

df = pd.read_csv("data.csv",sep=";")
col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images\{row['image']}" )
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images\{row['image']}" )
        st.write(f"[source code]({row['url']})")


