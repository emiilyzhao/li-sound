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
