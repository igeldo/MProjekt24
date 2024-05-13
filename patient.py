from person import Person


class Patient(Person):
    def __init__(self, name: str, surname: str, birthdate: str, abbreviation: str, PreIllness: str, Symptoms: str, Sex: str):
        super().__init__(name, surname, birthdate, abbreviation)
        self._preillness = PreIllness
        self._symptoms = Symptoms
        self._sex= Sex



    def show_attributes(self):
        super().show_attributes()
        print('Fachrichtung:', self._profession)
