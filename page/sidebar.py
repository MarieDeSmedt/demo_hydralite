import streamlit as st
import pandas as pd
import datetime

def display_sidebar():
    mon_perimetre={}

    #sector
    choosed_sector = st.sidebar.multiselect("SECTEURS:",st.session_state['authorised_sectors'])
    mon_perimetre["sector"] = choosed_sector

    #periode
    start = st.sidebar.date_input('start date :')
    end = st.sidebar.date_input('end date :')
    mon_perimetre["start"]=start
    mon_perimetre["end"]=end


    
    
    #siteCluster
    #typeTicket	
    #brandType	
    #segmentation>SegmentValue>SegmentLabel	
    #custAgeRange	
    #customerActivationEasinessLabel	

    if st.sidebar.button("définir périmètre"):
        st.session_state['mon_perimetre']= mon_perimetre



               
