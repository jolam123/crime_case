import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime


import plotly.express as px


@st.cache
def load_data():
    return pd.read_csv('hittakuri_revised.csv')

def run():
    st.title("Crime in Osaka in 2018")

    st.set_page_config(layout="wide")

    df = pd.read_csv('hittakuri_revised.csv')
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="town", hover_data=["crime_name", "crime_type"],
                        color_discrete_sequence=["fuchsia"], zoom=8)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    run()