from person import Person

class Doctor(Person):
    def __init__(self, profession: str):
       # super().__init__( name, surname, birthdate, abbreviation, age)
        self._profession = profession
