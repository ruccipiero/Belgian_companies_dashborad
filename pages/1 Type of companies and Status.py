import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
st.set_page_config(layout = 'wide')

#color = st.color_picker('Pick A Color', '#FF6464')
status_df = pd.read_csv('status_df.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]


st.markdown("# Type of companies and Status")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a2, a1= st.columns((3,2))
# Create distplot with custom bin_size
with a1:
    # This dataframe has 244 lines, but 4 distinct values for `day`
    st.markdown('### Companies status')    
    fig = px.pie(status_df, values='quantity_of_companies', names='Status')
    st.plotly_chart(fig, use_container_width=True)

with a2:
    st.markdown("### Percentage of the Companies: Type of Entreprise")
    fig = px.bar(TypeOfCompany_df, y="quantity_of_companies", x="TypeOfCompany", color='TypeOfCompany') #, marginal="rug")
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_xaxes(title_text='Type Of Company')
    fig.update_yaxes(title_text='Percentage of companies')
    # Plot!
    st.plotly_chart(fig, use_container_width=True)