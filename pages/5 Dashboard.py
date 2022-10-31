import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
st.set_page_config(layout = 'wide')

status_df = pd.read_csv('status_df.csv')
TypeOfCompany_df = pd.read_csv('TypeOfCompany_df.csv')
TypeOfCompany_df['TypeOfCompany'] =["Personne morale","Personne physique"]

color = st.color_picker('Pick A Color', '#139289')

st.markdown('# Dashboard')
a1, a2,a3  = st.columns((5, 3, 9))

# Create distplot with custom bin_size
with a1:
    # This dataframe has 244 lines, but 4 distinct values for `day`
    st.markdown('### Companies status')    
    fig = px.pie(status_df, values='quantity_of_companies',color_discrete_sequence=[color], names='Status', height=300)
    st.plotly_chart(fig, use_container_width=True)

with a2:
    st.markdown("### Type of Entreprise")
    fig = px.bar(TypeOfCompany_df, y="quantity_of_companies", x="TypeOfCompany", color='TypeOfCompany', 
        height=400) #, marginal="rug")
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_xaxes(title_text='Type Of Company')
    fig.update_yaxes(title_text='Percentage of companies')
    # Plot!
    st.plotly_chart(fig, use_container_width=True)

JuridicalForm_df = pd.read_csv('JuridicalForm_df_clean.csv')
JuridicalForm2_df=JuridicalForm_df[JuridicalForm_df['quantity_of_companies'] > 1]
JuridicalForm2_df['quantity_of_companies'] = round(JuridicalForm2_df['quantity_of_companies'])

with a3:
    st.markdown('### Main juridical forms ')
    fig = px.bar(JuridicalForm2_df, x='JuridicalForm', y='quantity_of_companies', 
        range_y=[0, 20], color='JuridicalForm', text="quantity_of_companies", height=500)#, width=1000)
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, 
        margin=dict(l=20, r=20, t=20, b=50))
    fig.update_yaxes(title_text='Percentage of companies')
    fig.update_xaxes(title_text='Juridical Form')
    st.plotly_chart(fig, use_container_width=True)


st.markdown('### All the juridical forms')
fig = px.bar(JuridicalForm_df, x='JuridicalForm', y='quantity_of_companies', text="quantity_of_companies", log_y=True,
    color_discrete_sequence=[color], width=1000, height=800)
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


sector_average_age_df = pd.read_csv( 'sector_average_age_df.csv')

# Row B
sector_average_age_df = sector_average_age_df.sort_values(by=['Description'])
sector_average_age_df = sector_average_age_df[sector_average_age_df['Age']>1]
jflist = sector_average_age_df['Description'].unique()
Nace_Code = st.selectbox("Select a Nace Code:",jflist)

b1, b2= st.columns((8,2))

with b1:
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

with b2:
    st.markdown('### Select a sector from above')

    fig = px.bar(sector_average_age_df[sector_average_age_df['Description'] == Nace_Code], 
        y = "Age", range_y=[0, 100], color_discrete_sequence=[color], text="Age", 
            hover_data=["NaceCode", "Number_of_Activities"])#, height=300)#, orientation = 'h') 
    fig.update_yaxes(title_text='Average age')
    fig.update_xaxes(showticklabels=False)
    st.plotly_chart(fig, use_container_width=True)
st.markdown(f' {Nace_Code}')


LanguageSearch_df = pd.read_csv( 'LanguageSearch_df.csv')
belgian_countries_df = pd.read_csv('belgian_regions.csv')
outer_countries_df = pd.read_csv('outer_countries.csv')


st.markdown("# Regions and Locatin overview")

c2, c1, c3= st.columns((1,1,3))
    # Create distplot with custom bin_size
with c1:
    
    st.markdown('### Language')
    fig = px.bar(LanguageSearch_df, y='PercentageDenominationLanguage', x='Language', height=500,
        text="PercentageDenominationLanguage", color='Language' )
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_yaxes(title_text='Percentage of languages')
    fig.update_xaxes(title_text='Language', categoryorder='array', 
        categoryarray= ['Dutch', 'French', 'Others','English', 'German'])
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown('### Regions')
    fig = px.bar(belgian_countries_df, x='Region', y='Count', width=500, height=500, text="Count", color = "Region" )
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_yaxes(title_text='Percentage of companies')
    fig.update_xaxes(title_text='Belgian region', categoryorder='array', categoryarray= ['Flanders', 'Wallonia', 'Bruxelles'])
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.markdown('### Companies with registered offices abroad')
    fig = px.bar(outer_countries_df, x='CountryFR', y='Count', width=1000, height=600, text="Count", 
        color = "CountryFR" ,log_y=True)
    fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'}, showlegend=False, margin=dict(l=20, r=20, t=20, b=30))
    fig.update_yaxes(title_text='Number of companies (logaritmic scale)')
    fig.update_xaxes(title_text='Countries', categoryorder='array', categoryarray= ['Bruxelles','Wallonia','Flanders'])
    st.plotly_chart(fig, use_container_width=True)
  


