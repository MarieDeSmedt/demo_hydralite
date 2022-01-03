
import streamlit as st
import hydralit_components as hc

from sidebar import display_sidebar


st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

display_sidebar()


menu_data = [
    {'label':"Synthèse"},
    {'label':"Analyse détaillée"},
    {'label':"Contexte"},
    {'label':"Analyse comparative"},
    {'label':"PMG"},
    {'label':"Segmentations"},
    {'label':"Points de vente"},
    {'label':"Contrôle"}
 ]

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    home_name='Home',
    sticky_nav=True, 
    sticky_mode='pinned'
)

if menu_id == "Synthèse":
    st.title("work in progress")
elif menu_id == "Analyse détaillée":
    st.title("work in progress")
elif menu_id == "Contexte":
    st.title("work in progress")
elif menu_id == "Analyse comparative":
    st.title("work in progress")
elif menu_id == "PMG":
    st.title("work in progress")
elif menu_id == "Segmentations":
    st.title("work in progress")
elif menu_id == "Points de vente":
    st.title("work in progress")
elif menu_id == "Contrôle":
    st.title("work in progress")
else:
    st.write("home")