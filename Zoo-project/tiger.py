"""
 **Klassenattribute**:
  - `num_appendages`: Die Anzahl der Extremitäten (Integer).
  - `is_cold_blooded`: Gibt an, ob das Tier kaltblütig ist (Boolean).
  - `is_mammal`: Gibt an, ob das Tier ein Säugetier ist (Boolean).

- **Überschriebene Methoden**:
  - Spezifiziere für jede Tierklasse angepasste Nachrichten für `eat()`, `sleep()`, und `grow(years)`.

"""
from tier import  Tier

class Tiger (Tier):
    def __init__(self,name,sex,age,num_appendages,is_cold_blooded,is_mammal):
        super().__init__(name,sex,age)
        self.num =num_appendages
        self.is_cold = is_cold_blooded
        self.is_mammal=is_mammal


    def eat(self,string):
         print(f"Tiger {self.name} frisst {string}.")

    def sleep(self,string):
         print(f'Tiger {self.name} schläft {string}.')

    def grow(self,years):
          print(f'Tiger {self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} jahre alt .')

    def bruellen(self):
        print(f"{self.name} brüllt laut und markiert sein Revier.")