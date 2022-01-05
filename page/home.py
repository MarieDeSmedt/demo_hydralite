import streamlit as st
import pandas as pd

def display_home():
    #affiche le message d'acceuil en fonction des secteurs auxquels la personne a accés
    df_sectors = pd.read_csv("data/sector_label.csv")
    authorised_sectors = st.session_state['authorised_sectors'].split("/")
    
    string_authorised_sectors = map(int, authorised_sectors)
    integer_authorised_sectors = list(string_authorised_sectors)
   
    df=df_sectors[df_sectors['sector'].isin(integer_authorised_sectors)]
    st.write("vous avez accés aux secteurs:")
    for index, row in df.iterrows():
        st.write(row[0],":", row[1])

