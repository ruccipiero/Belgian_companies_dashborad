import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

color = st.color_picker('Pick A Color', '#FF6464')
status_df = pd.read_csv('status_df.csv')
JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]
sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')

st.markdown("# Main page 🎈")


status_df = pd.read_csv('status_df.csv')
JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]
sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')
LanguageSearch_df = pd.read_csv( 'LanguageSearch_df.csv')
belgian_countries_df = pd.read_csv('belgian_regions.csv')
outer_countries_df = pd.read_csv('outer_countries.csv')



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a2, a1= st.columns((3,2))
# Create distplot with custom bin_size
with a1:
    # This dataframe has 244 lines, but 4 distinct values for `day`
    st.markdown('### Companies status')    
    fig = px.pie(status_df, values='quantity_of_companies', names='Status')

    #fig.update_xaxes(title_text='Time')
    #fig.update_yaxes(title_text='Value A')
    st.plotly_chart(fig, use_container_width=True)

with a2:
    st.markdown("### Percentage of the Companies: Type of Entreprise")
    fig = px.bar(TypeOfCompany_df, y="quantity_of_companies", x="TypeOfCompany", color='TypeOfCompany') #, marginal="rug")
    fig.update_xaxes(title_text='Type Of Company')
    fig.update_yaxes(title_text='Percentage of companies')
    # Plot!
    st.plotly_chart(fig, use_container_width=True)



st.markdown('### Juridical Form')
fig = px.bar(JuridicalForm_df, x='JuridicalForm', y='quantity_of_companies', text="quantity_of_companies", log_y=True,
                 width=1000, height=800)
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=30))
fig.update_yaxes(title_text='Percentage of companies (logaritmic scale)')
fig.update_xaxes(title_text='Juridical Form')
fig.add_shape( # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=1, y1=1, yref="y")
fig.add_annotation( # add a text callout with arrow
    text="Under 1%!", y=0.1, x='Société en commandite', arrowhead=1, showarrow=True)
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
fig = px.scatter(sector_average_age_df, x="NaceCode", y="Age", log_x=True, range_x=[1000, 10000000], 
    color = "Number_of_Activities", color_continuous_scale='rainbow'  )
fig.update_xaxes(title_text='Nace Code', constrain="domain",)
fig.update_yaxes(title_text='Age')
fig.update_traces(marker=dict(size=10), selector=dict(mode='markers'))

st.plotly_chart(fig, use_container_width=True)
