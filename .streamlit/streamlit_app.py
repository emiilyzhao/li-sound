import streamlit as st
import streamlit.components.v1 as components


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

path_to_html = "bottom-do.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Show an external HTML")
st.components.v1.html(html_data,height=200)
