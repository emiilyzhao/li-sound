import numpy as np
import pandas as pd
import folium 
import geopandas as gpd
import streamlit as st
import streamlit.components.v1 as components
from streamlit_folium import folium_static
from final_functions import mapping

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

surface_data = pd.read_csv('data/surface_water_quality.csv')
surface_time = folium_static(mapping(surface_data))

st.write("## Time Series")