import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
  


def display_login():
    data=pd.read_csv("data/login.csv")
    
    names = data['names']
    usernames = data['usernames']
    passwords =data['passwords'].astype(str)
    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=1)

    st.session_state['name'],st.session_state['authentication_status'] = authenticator.login('Login','sidebar')

    if st.session_state['authentication_status']:        
        st.write("welcome", st.session_state['name']) 
        #init authorised_sectors
        df =data.loc[(data['names'] == st.session_state['name'])]
        authorised_sectors = df['sectors'].iloc[0]
        string_authorised_sectors =  authorised_sectors.split("/")
        integer_authorised_sectors = map(int, string_authorised_sectors)
        st.session_state['authorised_sectors'] = list(integer_authorised_sectors)

    elif st.session_state['authentication_status'] == False:
        st.sidebar.error('Username/password is incorrect')

    elif st.session_state['authentication_status'] == None:
        st.sidebar.warning('Please enter your username and password')
        