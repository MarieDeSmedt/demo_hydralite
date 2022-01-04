import streamlit as st
import pandas as pd

def display_sidebar():
    df = pd.read_csv("data\Streamlit_test.csv")
    mon_perimetre={}
    for column in df:
        if column != "nbcust" and column != "salesQuantity" and column != "salesAmount":
            perimetre = st.sidebar.multiselect(column,df[column].unique())
            mon_perimetre[column] = perimetre
    if st.sidebar.button("définir périmètre"):
        st.session_state['mon_perimetre']=mon_perimetre



               
