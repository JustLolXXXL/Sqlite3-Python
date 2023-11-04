import sqlite3

db = sqlite3.connect('server.db')

# Create cursor
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS req (
    name TEXT,
    work TEXT,
    clock TEXT
)""")

def adm():
    c.execute("SELECT * FROM req")
    print(c.fetchall())

while True:
    name = input("Name: ")
    work = input("Work: ")
    clock = input("Time: ")

    c.execute(f"""INSERT INTO req VALUES ('{name}', '{work}', '{clock}')""")

    dsd = input("Password: ")
    if dsd == "Jou!":
        adm()

    db.commit()