import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
st.set_page_config(layout = 'wide')

sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("# Age sectors")


st.markdown('### Average age for every sector')
fig = px.scatter(sector_average_age_df, x="NaceCode", y="Age", log_x=True, range_x=[1000, 10000000], 
    hover_name="Description", color = "Number_of_Activities", color_continuous_scale='rainbow')
fig.update_layout(showlegend=False, #{'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'},  
    margin=dict(l=20, r=20, t=20, b=30))
fig.update_xaxes(title_text='Nace Code', constrain="domain",)
fig.update_yaxes(title_text='Average age')
fig.update_traces(marker=dict(size=10), selector=dict(mode='markers'))

st.plotly_chart(fig, use_container_width=True)

# # Selection Bar
sector_average_age_df = sector_average_age_df.sort_values(by=['Description'])
sector_average_age_df = sector_average_age_df[sector_average_age_df['Age']>1]

st.markdown('### Select a sector')
color = st.color_picker('Pick A Color', '#139289')

slist = sector_average_age_df['Description'].unique()
Nace_Code = st.multiselect(
    'Select a sector',
    slist,
    ['Enseignement secondaire professionnel ou technique organisé par les forces armées'])

st.markdown(f' {Nace_Code[0]}')
fig = px.bar(sector_average_age_df[sector_average_age_df['Description'] == Nace_Code[0]], 
    x = "Age", range_x=[0, 100], color_discrete_sequence=[color], text="Age", hover_data=["NaceCode", "Number_of_Activities"], 
    height=300) 
fig.update_yaxes(title_text='Average age')
fig.update_yaxes(showticklabels=False)
st.plotly_chart(fig, use_container_width=True)

Nace_Code = st.selectbox("Select a Nace Code:",slist)
st.markdown(f' {Nace_Code}')
fig = px.bar(sector_average_age_df[sector_average_age_df['Description'] == Nace_Code], 
    x = "Age", range_x=[0, 100], color_discrete_sequence=[color], text="Age", hover_data=["NaceCode", "Number_of_Activities"], 
    height=300) 
fig.update_yaxes(title_text='Average age')
fig.update_yaxes(showticklabels=False)
st.plotly_chart(fig, use_container_width=True)


