import sqlite3

def update_score(username, score):

    conn = sqlite3.connect("arcade.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET score = score + ? WHERE username=?", (score,username))
    conn.commit()
    conn.close()


def show_leaderboard():

    conn = sqlite3.connect("arcade.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username,score FROM users ORDER BY score DESC")
    rows = cursor.fetchall()

    print("\nLeaderboard")

    for r in rows:
        print(r[0],":",r[1])

    conn.close()