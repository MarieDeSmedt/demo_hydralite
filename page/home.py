import streamlit as st
import pandas as pd

def display_home():
    #affiche le message d'acceuil en fonction des secteurs auxquels la personne a accés
    df_sectors = pd.read_csv("data/sector_label.csv")
    df=df_sectors[df_sectors['sector'].isin(st.session_state['authorised_sectors'])]
    st.write("vous avez accés aux secteurs:")
    for index, row in df.iterrows():
        st.write(row[0],":", row[1])

