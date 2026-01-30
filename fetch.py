import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

# This trims the output to the COLUMNS in the databse
# query = """
#     SELECT playerID,yearID,teamID,HR
#     FROM batting
# """

# This trims the output to ROWS (the WHERE clause)
query = """
    SELECT playerID,yearID,teamID,HR
    FROM batting
    WHERE teamID = 'PHI' and yearID = 1976 and HR != 0
    ORDER BY HR desc
"""
# delete 'desc' if you want HR ordered lowest to highest

cursor.execute(query)
records = cursor.fetchall()
conn.close

records_df = pd.DataFrame(records, columns = ['playerID', 'yearID', 'teamID', 'HR'])
print(records_df)