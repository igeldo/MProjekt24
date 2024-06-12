from Model.blutbild import Blutbild
from person import Person


class Patient(Person):
    patient_counter = 0

    def __init__(self, name: str, surname: str, birthdate: str, phoneNumber: int, abbreviation: str, preIllness: str,
                 symptoms: str, sex: str):
        super().__init__(name, surname, birthdate, phoneNumber, abbreviation)
        self._preillness = preIllness
        self._symptoms = symptoms
        self._sex = sex
        Patient.patient_counter += 1
        self._patient_id = Patient.patient_counter
        self._Blutbilder = []


    def add_Blutbilder(self, blutbild: Blutbild):
        self._Blutbilder.append(blutbild)

    def get_preillness(self):
        return self._preillness

    def get_symptoms(self):
        return self._symptoms

    def get_sex(self):
        return self._sex

    def get_patient_id(self):
        return self._patient_id

    def get_Blutbilder(self):
        return [blutbild for blutbild in self._Blutbilder]

    def get_all(self):
        return [self._name, self._surname, self._birthdate, self._phoneNumber, self._abbreviation, self._preillness,
                self._symptoms, self._sex, self._patient_id]
