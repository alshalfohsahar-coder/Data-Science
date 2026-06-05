import sqlite3
from random import choice

db_path = r"E:\Data Science\python3\drittewoche\Aufgabe\database.db"

def insert_db(word:str , length:int):
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()

    insert_query = "insert into words values(?,?)"
    cur.execute(insert_query, (word,length))
    connection.commit()
    print(f"Das wort : {word} wird hinzfügen")

    connection.close()

while True : 
    wort = input("Welches wort soll die Datenbank hinzfügen ? oder q to exit  ")

    if wort == "q" :
        break
    insert_db((wort.upper()),len(wort))

