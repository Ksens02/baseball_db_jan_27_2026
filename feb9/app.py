import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT teamID, sum(HR)
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    HAVING sum(HR) >= 200;
"""
# query = """
#     SELECT playerID
#     FROM batting
#     WHERE playerID LIKE "ch%"
#     GROUP BY playerID
# """
# query = """
#     SELECT yearID, sum(HR)
#     FROM batting
#     WHERE teamID = "PHI"
#     GROUP BY yearID
#     ORDER BY sum(HR) desc
#     LIMIT 10;
# """

cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns = ['teamID', "totalHR"])
# df = pd.DataFrame(records, columns = ['yearID', 'totalHR'])
print(df)