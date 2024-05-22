from person import Person


class Patient(Person):
    # Statische Variable für die Patienten-ID
    patient_counter = 0

    def __init__(self, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str, preIllness: str, symptoms: str, sex: str):
        super().__init__(name, surname, birthdate,phoneNumber, abbreviation)
        self._preillness = preIllness
        self._symptoms = symptoms
        self._sex = sex

        # Neue Patienten-ID generieren
        Patient.patient_counter += 1
        self._patient_id = Patient.patient_counter

    def show_attributes(self):
        print('Patient: ',  self._patient_id)
        super().show_attributes()
        print('Vorerkrankung:', self._preillness)
        print('Symptome:', self._symptoms)
        print('Geschlecht:', self._sex)