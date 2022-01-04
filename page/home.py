import streamlit as st

def display_home(df_authorised_sectors):
    st.write("welcome", st.session_state['name'])
    st.write("vous avez accés aux secteurs:")
    st.table(df_authorised_sectors)

        
