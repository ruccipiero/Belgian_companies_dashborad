import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image


st.set_page_config(layout = 'wide')

# Data
#color = st.color_picker('Pick A Color', '#FF6464')
status_df = pd.read_csv('status_df.csv')
JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]
sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')
LanguageSearch_df = pd.read_csv( 'LanguageSearch_df.csv')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

b2, b1  = st.columns((3,2))
b1.image(Image.open('logo-becode.png'))
b2.markdown("""# Interactive dashborad

### Realiation of an interactive dashboard basing on: BANQUE-CARREFOUR DES ENTREPRISES""")

st.markdown("""
#### Team:

- Jack XIN

- Piero RUCCI
""")


def main_page():
    st.markdown("# Main page")
    st.sidebar.markdown("# Intro 🎈")

def page2():
    st.markdown("# Overview ")
    st.sidebar.markdown("# Overview ")

def page3():
    st.markdown("# Locations and languages ")
    st.sidebar.markdown("# Locations and languages ")

#page_names_to_funcs = {
#    "Overview": main_page,
#    "Insights": page2,
#    "Ending": page3,
#}
#
#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()






