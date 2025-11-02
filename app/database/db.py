import sqlite3

def create_table():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_msg TEXT,
            bot_msg TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_chat(user_msg: str, bot_msg: str):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (user_msg, bot_msg) VALUES (?, ?)", (user_msg, bot_msg))
    conn.commit()
    conn.close()

# Create table automatically when the app starts
create_table()
