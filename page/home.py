import streamlit as st

def display_home():
    st.write("welcome", st.session_state['name'])

    sectors = st.session_state['sectors'].split("/")
    if len(sectors)>1:
        st.write("vous avez accés aux secteurs:")
        for sector in sectors:
            st.write(sector)
    
        
