import sqlite3
from random import choice

db_path = r"E:\Data Science\python3\drittewoche\Aufgabe\database.db"
Max_versuch = 5

## function connet to the database and return the words with input length
def db_connection(letter_count: int):
  
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()

    query = "SELECT word FROM words WHERE letters = ?"
    words = cur.execute(query, (letter_count,)).fetchall()

    connection.close()
    return [w[0] for w in words]

### function get the lenght of word
def get_letter_count():
   
    while True:
        user_input = input("whäle die Anzahl der Buchtaben , welche wort enhalten soll oder q to Exit :  ").lower()

        if user_input == "q":
            return None

        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)

        print("Bitte, gib eine gültige Zahl ein.")

########## Main Function ################
def main():
    letter_count = get_letter_count()
    if letter_count is None:
        print("Spiel beendet.")
        return

    words = db_connection(letter_count)
    #print(words)
    if not words:
        print(" Kein Wort mit dieser Länge gefunden.")
        return

    word = choice(words)
    print (f" wort ist :{word}")
    guessed_letters = set()
    count = 0

   

    while count < Max_versuch:
        
        output = ""
        for char in word:
            if char in guessed_letters :
                 output += char
            else :
                output +="-"

        print("\n", output)
        print(f"Verbleibende Versuche: {Max_versuch - count}")

        if "-" not in output:
            print(" Geschafft!!! ")
            return

        letter = input("Welche Buchstabe wählst du? ").capitalize().strip()

        if not letter.isalpha() or len(letter) != 1:
            print("Bitte, gib einen Buchstaben ein.")
            continue

       

        guessed_letters.add(letter)

        if letter not in word:
            print(f"leider  {letter} ist nicht im Wort.")
            count += 1
        else:
            print(f"{letter} ist richtig!")

    print(f"\n Leider verloren! Das Wort war: {word}")



main()
