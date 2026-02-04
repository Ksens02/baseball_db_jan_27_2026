import sqlite3
import gradio as gr
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
# query = """
#     SELECT playerID,sum(HR) as careerHR
#     FROM batting
#     GROUP BY playerID
#     ORDER BY careerHR desc
#     LIMIT 11
# """

query = """
    SELECT teamID, yearID, sum(HR) as totalHR
    FROM batting
    WHERE teamID = "PHI"
    GROUP BY yearID
    ORDER BY yearID desc
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

# records_df = pd.DataFrame(records, columns = ['playerID', 'careerHR'])
records_df = pd.DataFrame(records, columns = ['teamID', 'yearID', 'totalHR'])
print(records_df)