import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

def display_home():

    data=pd.read_csv("data/login.csv")
    
    names = data['names']
    usernames = data['usernames']
    passwords =data['passwords'].astype(str)
    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

    # initialisation pour pouvoir se logout
    st.session_state['name'] ="init"
    st.session_state['authentication_status']=False

    st.session_state['name'],st.session_state['authentication_status'] = authenticator.login('Login','sidebar')

    if st.session_state['authentication_status']:
        st.sidebar.write('Welcome *%s*' % (st.session_state['name']))
    elif st.session_state['authentication_status'] == False:
        st.sidebar.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.sidebar.warning('Please enter your username and password')
    