import sqlite3
import gradio as gr


# create an app that allows a user to see the HR hit by players on the 1976 phillies
def fetch_phillies():
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' and yearID = 1976
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for player in records:
        players.append(player[0])
    return players


def f(player):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE playerID = ? and yearID = 1976 and teamID = 'PHI'
    """
    cursor.execute(query, [player])
    records = cursor.fetchall()
    return records[0][0]


with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = fetch_phillies(), interactive = True)
    HR = gr.Number(label = "Home Runs")
    playerID.change(fn = f, inputs = [playerID], outputs = [HR])

    
iface.launch()
