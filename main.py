
import streamlit as st
import hydralit_components as hc

from page.sidebar import display_sidebar
from page.synthese import display_synthese
from page.analyseComparative import display_analyseComparative
from page.analyseDetaillee import display_analyseDetaillee
from page.contexte import display_contexte
from page.controle import display_controle
from page.pmg import display_pmg
from page.pointsDeVente import display_pointDeVente
from page.segmentations import display_segmentations
from page.home import display_home

# toujours en premier
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

  

#Nom des onglets
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

#set the nevbar
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    home_name='Home',
    sticky_nav=True, 
    sticky_mode='pinned'
)

#action selon onglet
if menu_id == "Synthèse":
    display_synthese()
elif menu_id == "Analyse détaillée":
    display_analyseDetaillee()
elif menu_id == "Contexte":
    display_contexte()
elif menu_id == "Analyse comparative":
    display_analyseComparative()
elif menu_id == "PMG":
    display_pmg()
elif menu_id == "Segmentations":
    display_segmentations()
elif menu_id == "Points de vente":
    display_pointDeVente()
elif menu_id == "Contrôle":
    display_controle()
else:
    display_home()
    
#set the sidebar
if st.session_state['authentication_status']:
    display_sidebar()