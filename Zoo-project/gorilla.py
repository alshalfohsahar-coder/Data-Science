"""
*Spezifische Methoden**:
  - Überlege dir zusätzliche Funktionen für jede Kindklasse, wie z.B. `klettern()` für die Gorillaklasse.
"""

from tier import  Tier

class Gorilla (Tier):
    def __init__(self,name,sex,age,num_appendages,is_cold_blooded,is_mammal,is_kletter):
        super().__init__(name,sex,age)
        self.num =num_appendages
        self.is_cold = is_cold_blooded
        self.is_mammal=is_mammal
        self.is_kletter = is_kletter


    def eat(self,string):
         print(f'Gorilla {self.name} isst {string}.')

    def sleep(self,string):
         print(f'Gorilla {self.name} schläft {string}.')

    def grow(self,years):
          print(f'Gorilla {self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} jahre alt .')

    def klettern(self):
         if self.is_kletter == 1:

             print( f"Gorilla {self.name} kann klettern")
         else:
             print(f"Gorilla {self.name} kann nicht klettern")
         