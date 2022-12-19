import sqlite3
from pprint import pprint


db = sqlite3.connect('example.db')
cursor = db.cursor()

cursor.execute('''SELECT * FROM users''')
result = cursor.fetchone()
pprint(result)
pprint(cursor.fetchall()[1])

user = "Andrii"
cursor.execute('''SELECT * FROM users WHERE name = ? OR email = ?''', (user, "user_1@ukr.net"))
pprint(cursor.fetchall())


"""
# create DB
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
INSERT INTO users (name, email)
VALUES (
    "Andrii",
    "bezkrovnyyav@gmail.com"
)
''')

cursor.executescript('''
INSERT INTO users(name, email)
VALUES(
    "Andrii_1",
    "bezkrovnyyav+1@gmail.com"
);

INSERT INTO users(name, email)
VALUES(
    "Andrii_2",
    "bezkrovnyyav+2@gmail.com"
)
''')
users = [
    ("user_1", "user_1@ukr.net"),
    ("user_2", "user_2@ukr.net"),
    ("user_3", "user_3@ukr.net"),
]

cursor.executemany(''' INSERT INTO users(name, email) VALUES (?, ?)''', users)

db.commit()

"""
db.close()


