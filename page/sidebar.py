import streamlit as st
import pandas as pd


def display_sidebar():
    mon_perimetre={}
    sectorlabel_liste=[]

    #sector
    df = pd.read_csv("data/sector_label.csv")
    labels = df.set_index('sector')['sectorlabel'].to_dict()
    options = list(labels.keys())
    def format_func(sector):
        return labels[sector]
    mon_perimetre["sector"]= st.sidebar.multiselect("SECTEUR:",options=options,format_func=format_func)
    
    
    #periode
    mon_perimetre["start"]  = st.sidebar.date_input('DEBUT:')
    mon_perimetre["end"] = st.sidebar.date_input('FIN:')
     

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
        



               
