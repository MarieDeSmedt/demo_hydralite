import streamlit as st
import pandas as pd
import datetime

def display_sidebar():
    mon_perimetre={}

    #sector
    mon_perimetre["sector"]= st.sidebar.multiselect("SECTEUR:",st.session_state['authorised_sectors'])
    
    #periode
    start_date = st.sidebar.date_input('DEBUT:')
    end_date = st.sidebar.date_input('FIN:')
    if start_date < end_date:
        mon_perimetre["start"]  = start_date
        mon_perimetre["end"] = end_date
    else:
        st.error('Error: End date must fall after start date.')
    
    

    #siteCluster
    siteCluster=['CLU01','CLU02','CLU03','CLU04','CLU05','CLU06']
    mon_perimetre['siteCluster'] = st.sidebar.multiselect("CLUSTER",siteCluster)

    #typeTicket	
    typeTicket=['SUPER','HYPER','DRIVE']
    mon_perimetre['typeTicket'] = st.sidebar.multiselect("FORMAT:",typeTicket)

    #brandType
    brandType=['MP','MN','NO','PP','Autre']
    mon_perimetre['brandType'] = st.sidebar.multiselect("MARQUE:",brandType)

    #custAgeRange
    custAgeRange=['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70+']
    mon_perimetre['custAgeRange'] = st.sidebar.multiselect("AGE:",custAgeRange)

    #customerActivationEasinessLabel
    customerActivationEasinessLabel=['Non géolocalisés','Hors zone','Très facile','Très difficile','Difficile',
                                        'Moyen','Facile']
    mon_perimetre['customerActivationEasinessLabel'] = st.sidebar.multiselect("ACTIVATION:",customerActivationEasinessLabel)

    #segmentation>SegmentValue>SegmentLabel	
    #TODO	
    	
    if st.sidebar.button("définir périmètre"):
        st.session_state['mon_perimetre']= mon_perimetre
        



               
