import sqlite3
from datetime import datetime

db = sqlite3.connect('server.db')

# Create cursor
c = db.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS reg (
    work TEXT,
    name TEXT,
    clock TEXT
)""")
# Creating functions for next steps
def adm():# Function for admins with password
    if dsd == "Jou!":
        c.execute("SELECT * FROM reg")
        print(c.fetchall())

def ntime():# Function, which check is time ... so delete all in table
    t = datetime.now()
    if t.strftime('%H:%M:%S') == '23:59:59':
        c.execute("DELETE FROM reg")

def check():# Function for cheking is name already in table in not so add to table
    c.execute(f"SELECT name FROM reg")
    rows = c.fetchall()
    l = []
    for row in rows:
        for x in row:
            l.append(x)
    if name1 in l:
        c.execute(f"UPDATE reg SET work = '{work1}' WHERE name = '{name1}'")
    else:
        c.execute(f"""INSERT INTO reg VALUES ('{work1}', '{name1}', '{clock1}')""")

# Cycle for 24/7 working
while True:
    # Using time function
    ntime()

    # Getting data
    name1 = input("Name: ")
    work1 = input("Work: ")
    clock1 = input("Time: ")

    # Using check function
    check()

    dsd = input("Password: ")
    #Using admin function
    adm()

    db.commit()