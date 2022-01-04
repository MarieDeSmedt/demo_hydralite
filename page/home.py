import streamlit as st

def display_home(df):
    st.write("welcome", st.session_state['name'])
    st.write("vous avez accés aux secteurs:")

    for index, row in df.iterrows():
        st.write(row[0],":", row[1])

