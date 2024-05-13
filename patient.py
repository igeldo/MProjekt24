from person import Person


class Patient(Person):
    # Statische Variable für die Patienten-ID
    patient_counter = 0

    def __init__(self, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str, PreIllness: str, Symptoms: str, Sex: str):
        super().__init__(name, surname, birthdate, phoneNumber, abbreviation)
        self._phoneNumber = phoneNumber
        self._preillness = PreIllness
        self._symptoms = Symptoms
        self._sex = Sex

        # Neue Patienten-ID generieren
        Patient.patient_counter += 1
        self._patient_id = Patient.patient_counter

    def show_attributes(self):
        print('Patient: ',  self._patient_id)
        super().show_attributes()
        print('Vorerkrankung:', self._preillness)
        print('Symptome:', self._symptoms)
        print('Geschlecht:', self._sex)
        print('Telefon: ', self._phoneNumber)