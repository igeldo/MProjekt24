from person import Person


class Doctor(Person):
    def __init__(self, title: str,  name: str, surname: str, birthdate: str, phoneNumber: int,  abbreviation: str, profession: str):
        super().__init__(name, surname, birthdate, phoneNumber, abbreviation)
        self._profession = profession
        self._title = title

    def getProfession(self):
        return self._profession

    def getTitle(self):
        return self._title
