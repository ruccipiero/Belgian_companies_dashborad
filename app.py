import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(layout = 'wide')

# Data
color = st.color_picker('Pick A Color', '#FF6464')
status_df = pd.read_csv('status_df.csv')
JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]
sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')
LanguageSearch_df = pd.read_csv( 'LanguageSearch_df.csv')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()






