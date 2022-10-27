# loading in modules
import sqlite3
import pandas as pd
import streamlit as st

# creating file path
dbfile = "bce.db"
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [
    a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
]
# here is you table list
print(table_list)

# Be sure to close the connection

df = pd.read_sql_query(
    """

SELECT *

FROM activity AS a1
INNER JOIN enterprise AS e1
ON a1.EntityNumber = e1.EnterpriseNumber

""",
    con,
)

# print(df)
print(df.head())
con.close()
