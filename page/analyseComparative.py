import streamlit as st


def display_analyseComparative():
    if st.session_state['mon_perimetre']:
        st.write(st.session_state['mon_perimetre'])
    else:
        st.write("veuillez définir un périmètre")