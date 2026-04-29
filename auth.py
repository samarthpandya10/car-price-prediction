import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
    """)

    # default admin
    c.execute("INSERT OR IGNORE INTO users VALUES (1,'admin','admin123','admin')")

    conn.commit()
    conn.close()


def login_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    data = c.fetchone()

    conn.close()
    return data


def signup_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO users(username,password,role) VALUES (?,?,?)",
              (username, password, "user"))

    conn.commit()
    conn.close()
