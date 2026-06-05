""" **Instanzattribute**:
  - `name`: Der Name des Tieres (String).
  - `sex`: Das Geschlecht des Tieres (Boolean, wobei `0` für männlich und `1` für weiblich steht).
  - `age`: Das Alter des Tieres (Integer).

- **Methoden**:
  - `eat()`: Gibt eine Nachricht aus, dass das Tier isst (z.B. "Max isst.").
  - `sleep()`: Gibt eine Nachricht aus, dass das Tier schläft (z.B. "Max schläft.").
  - `grow(years)`: Erhöht das Alter des Tieres um `years` Jahre und gibt eine Nachricht aus (z.B. "Max wurde 5 Jahre älter und ist jetzt 20 Jahre alt.").
  """

class Tier :
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
      
    def eat(self,string):
         print(f"{self.name}  {string}.")

    def sleep(self,string):
         print(f"{self.name} {string}.")

    def grow(self,years):
          print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} jahre alt .")
        