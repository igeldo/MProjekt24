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

    def getPreIllness(self):
        return self._preillness

    def getSymptoms(self):
        return self._symptoms

    def getSex(self):
        return self._sex

    def getPatientId(self):
        return self._patient_id

    def getAll(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation, self._preillness, self._symptoms, self._sex, self._patient_id]