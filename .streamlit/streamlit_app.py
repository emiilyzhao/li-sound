<<<<<<< HEAD
import streamlit as st
import streamlit.components.v1 as components

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

graph = open('/Users/emilyzhao/li-sound/mapping/surface-do.html')
components.html(graph.read())

=======
import numpy as np
import pandas as pd
import streamlit as st
from final_functions import mapping, time_series

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

surface_data = pd.read_csv('data/surface_water_quality.csv')
surface_time = folium_static(mapping(surface_data))

st.write("## Time Series")
>>>>>>> 22d3fcc0f8df05ac8c62705b3808c88cc1464f9a
