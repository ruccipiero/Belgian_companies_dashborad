import streamlit as st
import sqlite3
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

a2, a1, a3= st.columns((3,2,5))
# Create distplot with custom bin_size
with a1:
    # This dataframe has 244 lines, but 4 distinct values for `day`
    st.markdown('### Companies status')    
    fig = px.pie(status_df, values='quantity_of_companies', names='Status')
    st.plotly_chart(fig, use_container_width=True)

with a2:
    st.markdown("### Percentage of the Companies: Type of Entreprise")
    fig = px.histogram(TypeOfCompany_df, y="quantity_of_companies", x="TypeOfCompany", color='TypeOfCompany' , marginal="rug",
                   hover_data=TypeOfCompany_df.columns)
    # Plot!
    st.plotly_chart(fig, use_container_width=True)


with a3:
    st.markdown('### Percentage of the Companies: Juridical Form')
    fig = px.pie(JuridicalForm_df, values='quantity_of_companies', names='JuridicalForm')
    st.plotly_chart(fig, use_container_width=True)

# # Selection Bar
#jflist = JuridicalForm_df['JuridicalForm'].unique()
#JuridicalForm = st.sidebar.selectbox("Select a Juridical Form:",jflist)
#fig = px.bar(JuridicalForm_df[JuridicalForm_df['JuridicalForm'] == JuridicalForm], 
#x = "quantity_of_companies", y = "JuridicalForm")   

#
#
## Page setting
#
## Row B
st.markdown('### Sector average age')
fig = px.scatter(sector_average_age_df, x="NaceCode", y="Age", hover_name="Number_of_Activities", log_x=True)
st.plotly_chart(fig, use_container_width=True)


st.markdown('LanguageSearch_df')
# fig = px.pie(LanguageSearch_df, values='DenominationLanguage', names='Language')
# st.plotly_chart(fig, use_container_width=True)
fig = px.histogram(LanguageSearch_df, y='PercentageDenominationLanguage', x='Language', color='Language' , marginal="rug")
# Plot!
st.plotly_chart(fig, use_container_width=True)

