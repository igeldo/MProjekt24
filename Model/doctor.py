from Model.person import Person


class Doctor(Person):
    # nimmt mehrere Parameter entgegen, die zur Initialisierung des Objekts verwendet werden.
    def __init__(self, title: str, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str,
                 profession: str):
        super().__init__(name, surname, birthdate, phoneNumber, abbreviation) # Konstruktor für die Basiseigenschaften der Ärzte.
        self._profession = profession # Hier wird die Instanzvariable _profession mit dem übergebenen profession Wert initialisiert.
        self._title = title

    def get_profession(self):
        return self._profession
        # Diese Methode gibt den Wert der Instanzvariable _profession des Doktor-Objekts zurück.

    def get_title(self):
        return self._title

    def get_all(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation, self._profession,
                self._title]
        # Diese Methode gibt eine Liste mit allen Attributen des Doktor-Objekts zurück,
        # einschließlich der von der Elternklasse geerbten Attribute.