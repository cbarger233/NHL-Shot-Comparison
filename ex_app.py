import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
goals_players = pd.read_csv('goals_players.csv')
selections = goals_players['full_shooter_name'].sort_values().unique().tolist()

from plot_shots import *

st.title('Compare NHL Players\' Shots')
st.markdown(
    """This data was obtained from Kaggle [here](https://www.kaggle.com/datasets/martinellis/nhl-game-data).
    Currently, there is only data available from the 2000-2001 season up until the end of the 2019-2021 season.
    \n\nNot all players are available to compare, as I cut down the choices to only include the top 829 players with the most amount of shots.
    This ensures that each player featured has at least 700 shots recorded during this timeframe.
    \n\nThe data collected by the NHL is only accurate to the nearest foot, and even then there is a huge amount of uncertainty.
    Because of this many of the shots overlap with each other."""
)
col1, col2 = st.columns(2)

with col1:
    choice1 = st.selectbox('Pick a player:', selections, key=1)
    distance1 = st.slider('Pick a shot distance:', 0, 189, key=2)

with col2:
    choice2 = st.selectbox('Pick a player:', selections, key=3)
    distance2 = st.slider('Pick a shot distance:', 0, 189, key=4)

clicked = st.button('Generate Plot')

if clicked:
    
    f1, info1 = plot_distance(choice1, goals_players, distance=distance1)
    f2, info2 = plot_distance(choice2, goals_players, distance=distance2)

    with col1:
        st.pyplot(f1)
        st.text(info1)

    with col2:
        st.pyplot(f2)
        st.text(info2)

    st.pyplot(f1)
    st.pyplot(f2)