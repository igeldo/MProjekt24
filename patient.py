from person import Person


class Patient(Person):
    # Statische Variable für die Patienten-ID
    patient_counter = 0

    def __init__(self, name: str, surname: str, birthdate: str, abbreviation: str, PreIllness: str, Symptoms: str, Sex: str):
        super().__init__(name, surname, birthdate, abbreviation)
        self._preillness = PreIllness
        self._symptoms = Symptoms
        self._sex= Sex

        # Neue Patienten-ID generieren
        Patient.patient_counter += 1
        self._patient_id = Patient.patient_counter

    def show_attributes(self):
        super().show_attributes()
        print('Patienten-ID:', self._patient_id)
        print('Vorerkrankung:', self._preillness)
        print('Symptome:', self._symptoms)
        print('Geschlecht:', self._sex)
