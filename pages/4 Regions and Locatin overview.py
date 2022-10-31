import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
st.set_page_config(layout = 'wide')

LanguageSearch_df = pd.read_csv( 'LanguageSearch_df.csv')
belgian_countries_df = pd.read_csv('belgian_regions.csv')
outer_countries_df = pd.read_csv('outer_countries.csv')

st.markdown("# Regions and Locatin overview")

a2, a1= st.columns((1,1))
    # Create distplot with custom bin_size
with a1:
    
    st.markdown('### Language')
    fig = px.bar(LanguageSearch_df, y='PercentageDenominationLanguage', x='Language', height=400,
        text="PercentageDenominationLanguage", color='Language' )
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_yaxes(title_text='Percentage of languages')
    fig.update_xaxes(title_text='Language', categoryorder='array', categoryarray= ['Dutch', 'French', 'Others','English', 'German'])
    st.plotly_chart(fig, use_container_width=True)

with a2:

    st.markdown('### Regions')
    fig = px.bar(belgian_countries_df, x='Region', y='Count', width=500, height=400, text="Count", color = "Region" )
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_yaxes(title_text='Percentage of companies')
    fig.update_xaxes(title_text='Belgian region', categoryorder='array', categoryarray= ['Flanders', 'Wallonia', 'Bruxelles'])
    st.plotly_chart(fig, use_container_width=True)

st.markdown('## Companies with registered offices abroad')
fig = px.bar(outer_countries_df, x='CountryFR', y='Count', width=1000, height=800, text="Count", color = "CountryFR" ,log_y=True)
fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, margin=dict(l=20, r=20, t=20, b=30))
fig.update_yaxes(title_text='Number of companies (logaritmic scale)')
fig.update_xaxes(title_text='Countries', categoryorder='array', categoryarray= ['Bruxelles','Wallonia','Flanders'])

st.plotly_chart(fig, use_container_width=True)
  