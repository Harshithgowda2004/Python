import sqlite3

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("arcade.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))
        conn.commit()
        print("Registration successful!")
    except:
        print("User already exists")

    conn.close()


def login():
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("arcade.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login Successful!")
        return username
    else:
        print("Invalid login")
        return None