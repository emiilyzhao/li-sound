import folium 
import geopandas as gpd
import numpy as np
import pandas as pd
import os
import json 
import datetime
import folium.plugins
from folium.plugins import TimeSliderChoropleth
from folium.plugins import HeatMapWithTime
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def heat_data(data):
    heat_data = []
    current_date = None
    current_sublist = []
    for _, row in data.iterrows():
        date = row['DATE']
        coordinates = (row['LON'], row['LAT'])
        weight = 1-float(row['DISSOLVED_OXYGEN_MG_L'] / data['DISSOLVED_OXYGEN_MG_L'].max())
        
        if pd.notnull(date) and pd.notnull(coordinates) and pd.notnull(weight):
            if date != current_date:
                if current_sublist:
                    heat_data.append(current_sublist)
                current_sublist = []
                current_date = date
            
            # switch lat and lon
            current_sublist.append([coordinates[1], coordinates[0], weight])

    if current_sublist:
        heat_data.append(current_sublist)

    return heat_data

def map(data):
    df = heat_data(data)
    index = [s.strip()[:8] for s in data['DATE'].unique()]
    map = folium.Map(location=[40.979142, -73.08496], zoom_start=10)
    heatmap = HeatMapWithTime(df, index=index, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'yellow', 0.9: 'red'}, radius = 40)
    heatmap.add_to(map)
    return map

def time_series(data):
    index = [s.strip()[:8] for s in data['DATE'].unique()]
    fig = go.Figure(data=go.Scatter(x=index, y=data['DISSOLVED_OXYGEN_MG_L'], mode='lines'))
    fig.update_layout(title='Time Series of Dissolved Oxygen', xaxis_title='Index', yaxis_title='Dissolved Oxygen (mg/L)')
    return fig
