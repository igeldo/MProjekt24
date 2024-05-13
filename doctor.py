from person import Person

class Doctor(Person):
    def __init__(self, name: str, surname: str, birthdate: str, abbreviation: str, profession: str):
        super().__init__(name, surname, birthdate, abbreviation)
        self._profession = profession

    def show_attributes(self):
        super().show_attributes()
        print('Fachrichtung:', self._profession)

