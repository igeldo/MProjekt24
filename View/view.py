from Model.doctor import Doctor
from Model.patient import Patient


class View:
    def __init__(self, model):
        self._model = model

    def display_person(self, person):
        if isinstance(person, Patient):
            self.display_patient(person)
        elif isinstance(person, Doctor):
            self.display_doctor(person)
        else:
            self.display_generic_person(person)

    def display_patient(self, patient):
        print(f"Patient ID: {patient.get_patient_id()}")
        print(f"Name: {patient.get_name()}")
        print(f"Surname: {patient.get_surname()}")
        print(f"Birthdate: {patient.get_birthdate()}")
        print(f"Abbreviation: {patient.get_abbreviation()}")
        print(f"Age: {patient.get_age()}")
        print(f"Sex: {patient.get_sex()}")
        print(f"Phone Number: {patient.get_phone_number()}")
        print(f"Pre-Illness: {patient.get_preillness()}")
        print(f"Symptoms: {patient.get_symptoms()}")
        print('\n')
        print("Blutbilder des Patienten:")
        for blutbild in patient.get_Blutbilder():
            print(f"Aufnahmedatum: {blutbild.getDate()}")
            for result in blutbild.checkMesswerte():
                print(f"{result[0]}: {result[1]} ({result[2]})")
        print('\n')

    def display_doctor(self, doctor):
        print(f"Title: {doctor.get_title()}")
        print(f"Name: {doctor.get_name()}")
        print(f"Surname: {doctor.get_surname()}")
        print(f"Abbreviation: {doctor.get_abbreviation()}")
        print(f"Birthdate: {doctor.get_birthdate()}")
        print(f"Age: {doctor.get_age()}")
        print(f"Phone Number: {doctor.get_phone_number()}")
        print(f"Profession: {doctor.get_profession()}")
        print('\n')

    def display_generic_person(self, person):
        print(f"Name: {person.get_name()}")
        print(f"Surname: {person.get_surname()}")
        print(f"Birthdate: {person.get_birthdate()}")
        print(f"Phone Number: {person.get_phone_number()}")
        print(f"Abbreviation: {person.get_abbreviation()}")
        print(f"Age: {person.get_age()}")
        print('\n')

    def display_blutbild(self, blutbild):
        print(f"Patienten ID: {blutbild.getPatID()}")
        print(f"Aufnahmedatum: {blutbild.getDate()}")
        print(f"Messwerte: {blutbild.getMesswerte()}")
