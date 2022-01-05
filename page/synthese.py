import pandas as pd
import streamlit as st


def display_synthese():
    
    if st.session_state['result']:
        st.write(st.session_state['result'])
    else:
        st.write("veuillez définir un périmètre")