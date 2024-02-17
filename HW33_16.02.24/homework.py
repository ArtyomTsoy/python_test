import sqlite3

connection = sqlite3.connect("C:\github\ArtyomTsoy\HW33_16.02.24\homework.py")
cursor = connection.cursor()

def read_all_rows():
    cursor.execute("SELECT * FROM bubu;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def read_one_row(condition):
    cursor.execute(f"SELECT * FROM bubu WHERE {condition};")
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Строка не найдена")

read_all_rows()
read_one_row("id = 1")

connection.close()