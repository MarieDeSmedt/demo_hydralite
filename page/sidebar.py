import streamlit as st
import pandas as pd

def display_sidebar():
    mon_perimetre={}

    #choose sector
    choosed_sector = st.sidebar.multiselect("SECTEURS:",st.session_state['authorised_sectors'])
    mon_perimetre["sector"] = choosed_sector

    if st.sidebar.button("définir périmètre"):
        st.session_state['mon_perimetre']= mon_perimetre



               
