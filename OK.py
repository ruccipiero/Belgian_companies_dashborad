import sqlite3
import os
import pandas as pd

connexion = sqlite3.connect("bce.db")
cursor = connexion.cursor()

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

cursor.execute(TypeOfCompany)
print(cursor.fetchall())
