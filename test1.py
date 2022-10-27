import sqlite3
import os
import pandas as pd
import streamlit as st
import plost

# creating file path
dbfile = "bce.db"
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()


status = """
    SELECT
        Status, (COUNT(*)/18632.92) AS quantity_of_companies
    FROM
        enterprise
	GROUP BY status
"""

JuridicalForm = """

    SELECT
        JuridicalForm, (COUNT(*)/18632.92) AS quantity_of_companies
    FROM
        enterprise
	GROUP BY JuridicalForm
	ORDER BY quantity_of_companies DESC

"""

TypeOfCompany = """

    SELECT
        TypeOfEnterprise, (COUNT(*)/18632.92) AS quantity_of_companies
    FROM
        enterprise
	GROUP BY TypeOfEnterprise
	ORDER BY quantity_of_companies DESC

"""

Age_of_company = """

SELECT *

FROM activity AS a1
INNER JOIN enterprise AS e1
ON a1.EntityNumber = e1.EnterpriseNumber

"""

sector_average_age = """

    SELECT
        c1.Description, a1.NaceCode, AVG(2022 - strftime('%Y',e1.StartDate)) AS "Age", COUNT(EntityNumber) AS Number_of_Activities
    FROM activity AS a1

    LEFT JOIN enterprise AS e1     ON  a1.EntityNumber = e1.EnterpriseNumber
    LEFT JOIN code AS c1 ON a1.NaceCode = c1.Code
    WHERE c1.Language LIKE "FR"
    GROUP BY NaceCode
    ORDER BY Age DESC

"""

status_df = pd.read_sql_query( status   , con)
JuridicalForm_df = pd.read_sql_query( JuridicalForm   , con)
TypeOfCompany_df = pd.read_sql_query( TypeOfCompany   , con)
sector_average_age_df = pd.read_sql_query( sector_average_age   , con)

st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a1, a2, a3= st.columns(3)
a1.metric("Wind", "9 mph", "-8%")
with a2:
    st.markdown('### Bar chart')
    plost.bar_chart(
        data=TypeOfCompany_df,##
        bar=TypeOfCompany_df.iloc[:,0],value=TypeOfCompany_df.iloc[:,1])

with a3:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=JuridicalForm_df,##
        theta='quantity_of_companies',
        color='JuridicalForm')

b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# def form():
#     st.write("This is a form")
#     with st.form(key="info form"):
#         name = st.text_input("enter name :")


# form()

cur.execute(JuridicalForm)
print(cur.fetchall())
con.close()

