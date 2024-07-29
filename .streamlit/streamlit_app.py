import streamlit as st
import streamlit.components.v1 as components


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#graph = open('/Users/emilyzhao/li-sound/mapping/surface-do.html')
#components.html(graph.read())

plot_file = open('/Users/emilyzhao/li-sound/mapping/surface-do.html','r')

plot = plot_file.read()

st.markdown(plot,unsafe_allow_html=True)

plot = plot_file.close()
