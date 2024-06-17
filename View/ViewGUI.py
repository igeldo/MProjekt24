from Model.doctor import Doctor
from Model.patient import Patient


class ViewGUI:
    def __init__(self, model):
        self._model = model

    def display_allData(self, gui):
        try:
            personen = self._model.get_Personen()

            result_text = "Alle Personen:\n"
            for person in personen:
                result_text += f"{self.display_person(person)}"
                result_text += ' \n'

            result_text += 'alle Blutbilder: \n'
            result_text += f"{self.display_blutbilder()}"

            gui.resultLabel.setText(result_text)
        except Exception as e:
            gui.resultLabel.setText(f"Fehler: {e}")
            print(f"Fehler in display_allData: {e}")

    def display_person(self, person):
        if isinstance(person, Patient):
            return self.display_patient(person)
        elif isinstance(person, Doctor):
            return self.display_doctor(person)

    def display_patient(self, patient):
        text = ""
        text += f"Patient ID {patient.get_patient_id()}: {patient.get_name()} {patient.get_surname()} ({patient.get_abbreviation()})\n"
        text += f"Birthdate: {patient.get_birthdate()}; {patient.get_age()} \n"
        text += f"Sex: {patient.get_sex()} \n"
        text += f"Phone Number: {patient.get_phone_number()} \n"
        text += f"Pre-Illness: {patient.get_preillness()} \n"
        text += f"Symptoms: {patient.get_symptoms()} \n"
        text += "Blutbilder des Patienten: \n"
        for blutbild in patient.get_Blutbilder():
            text += f"Aufnahmedatum: {blutbild.getDate()} \n"
            for result in blutbild.checkMesswerte():
                text += f"{result[0]}: {result[1]} ({result[2]}) | "
            text += '\n'
        text += '\n'

        return text

    def display_doctor(self, doctor):
        text = ""
        text += f"{doctor.get_abbreviation()}: {doctor.get_title()} {doctor.get_name()} {doctor.get_surname()} \n"
        text += f"Birthdate: {doctor.get_birthdate()}; Age: {doctor.get_age()} \n"
        text += f"Profession: {doctor.get_profession()} \n"

        return text

    def display_blutbilder(self):
        text = ""
        blutbilder = self._model.get_Blutbilder()
        for blutbild in blutbilder:
            text += f"ID: {blutbild.getPatID()}, Datum: {blutbild.getDate()} \n"
            text += f"Messwerte: {blutbild.getMesswerte()} \n"

        return text
