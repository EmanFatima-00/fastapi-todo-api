import sqlite3

DB_NAME = "tasks.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # taake result dict ki tarah mile
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    # 1. Table banao
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  done BOOLEAN DEFAULT 0)''')

    # 2. Check karo 3 tasks pehle se hain ya nahi
    c.execute("SELECT COUNT(*) FROM tasks")
    if c.fetchone()[0] == 0:
        # 3. Agar nahi hain to ye 3 daal do
        c.executemany("INSERT INTO tasks (title, done) VALUES (?,?)",
                      [("Learn FastAPI", 0),
                       ("Connect Database", 0),
                       ("Submit Assignment", 0)])

    conn.commit()
    conn.close()