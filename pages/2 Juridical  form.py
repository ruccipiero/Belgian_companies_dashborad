import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
st.set_page_config(layout = 'wide')

JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
JuridicalForm2_df=JuridicalForm_df[JuridicalForm_df['quantity_of_companies'] > 1]
JuridicalForm2_df['quantity_of_companies'] = round(JuridicalForm2_df['quantity_of_companies'] ,2)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown("# Juridical form")

st.markdown('### Main juridical forms')
fig = px.bar(JuridicalForm2_df, x='JuridicalForm', y='quantity_of_companies', 
    range_y=[0, 20], color='JuridicalForm', text="quantity_of_companies", height=500)#, width=1000)
fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, 
    margin=dict(l=20, r=20, t=20, b=40))
fig.update_yaxes(title_text='Percentage of companies')
fig.update_xaxes(title_text='Juridical Form')
st.plotly_chart(fig, use_container_width=True)


st.markdown('### Percentage of the Companies: juridical form?')
fig = px.bar(JuridicalForm_df, x='JuridicalForm', y='quantity_of_companies', text="quantity_of_companies", log_y=True,
                 width=1000, height=800)
fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, 
    margin=dict(l=20, r=20, t=20, b=50))
fig.update_yaxes(title_text='Percentage of companies (logaritmic scale)')
fig.update_xaxes(title_text='Juridical Form')
fig.add_shape( # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=1, y1=1, yref="y")
fig.add_annotation( # add a text callout with arrow
    text="Under 1%!", y=0.1, x='Société en commandite', arrowhead=1, showarrow=True)
st.plotly_chart(fig, use_container_width=True)

