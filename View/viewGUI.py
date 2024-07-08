from Model.doctor import Doctor
from Model.patient import Patient


class ViewGUI:
    def __init__(self, model):
        self._model = model
    # Konstruktor der Klasse View
    # nimmt ein model-Objekt entgegen, das Daten über die darzustellenden Personen enthält.

    def display_allData(self, gui): # alle Personen und Blutbilder, die im Modell gespeichert sind, werdenin einem GUI-Element (der resultLabel) auszugeben.
        try: # Try-Except-Block, um Ausnahmen abzufangen, die während der Ausführung auftreten können
            personen = self._model.get_Personen() # Liste aller Personen aus dem Modell abgerufen

            result_text = "Alle Personen:\n"
            for person in personen: # wird eine Schleife über alle Personen in der Liste durchlaufen.
                result_text += f"{self.display_person(person)}"
                # Für jede Person wird die display_person-Methode aufgerufen,
                # um eine textuelle Darstellung der Person zu erhalten.
                # Das Ergebnis wird an result_text angehängt.
                result_text += ' \n'

            result_text += 'alle Blutbilder: \n'
            result_text += f"{self.display_blutbilder()}"

            gui.resultLabel.setText(result_text)
            # Nachdem die gesamte Darstellung in result_text zusammengestellt wurde,
            # wird der Text in das GUI-Element resultLabel geschrieben,
            # sodass es dem Benutzer angezeigt wird.
        except Exception as e:
            # Wenn während der Ausführung eine Ausnahme auftritt,
            # wird der Fehlertext in das resultLabel geschrieben
            # und zusätzlich auf der Konsole ausgegeben.
            gui.resultLabel.setText(f"Fehler: {e}")
            print(f"Fehler in display_allData: {e}")

    def display_person(self, person): # Darstellung einer Person (entweder ein Patient oder ein Arzt)
        if isinstance(person, Patient): # Zunächst wird überprüft, ob die übergebene person ein Instanz der Klasse Patient ist.
            return self.display_patient(person)
        elif isinstance(person, Doctor): # Wenn die person keine Instanz von Patient ist, wird überprüft, ob sie eine Instanz der Klasse Doctor ist
            return self.display_doctor(person) # Rückgabe über display_person-Methode

    def display_patient(self, patient):
        text = "" #  leere Zeichenkette text initialisiert, in der das Ergebnis zusammengestellt wird
        text += f"Patient ID {patient.get_patient_id()}: {patient.get_name()} {patient.get_surname()} ({patient.get_abbreviation()})\n"
        # erste Teil der Patientendarstellung wird erstellt, der die Patienten-ID, den Vornamen, den Nachnamen und die Abkürzung enthält.
        text += f"Birthdate: {patient.get_birthdate()}; {patient.get_age()} \n"
        # Geburtsdatum und das Alter des Patienten hinzugefügt.
        text += f"Sex: {patient.get_sex()} \n"
        text += f"Phone Number: {patient.get_phone_number()} \n"
        text += f"Pre-Illness: {patient.get_preillness()} \n"
        text += f"Symptoms: {patient.get_symptoms()} \n"
        text += "Blutbilder des Patienten: \n"
        # Überschrift für die Blutbilder des Patienten
        # Schleife über alle Blutbilder des Patienten durchlaufen.
        for blutbild in patient.get_Blutbilder():
            text += f"Aufnahmedatum: {blutbild.getDate()} \n" # Für jedes Blutbild wird das Aufnahmedatum hinzugefügt.
            for result in blutbild.checkMesswerte(): # weitere Schleife über die einzelnen Messwerte des Blutbilds durchlaufen.
                text += f"{result[0]}: {result[1]} ({result[2]}) | " # Für jeden Messwert wird der Name, der Wert und die Einheit hinzugefügt.
            text += '\n'
        text += '\n'

        return text
        # Nachdem die gesamte Patientendarstellung in text zusammengestellt wurde,
        # wird diese Zeichenkette als Ergebnis zurückgegeben.

    def display_doctor(self, doctor):
        text = ""
        text += f"{doctor.get_abbreviation()}: {doctor.get_title()} {doctor.get_name()} {doctor.get_surname()} \n"
        # rste Teil der Arztdarstellung erstellt, der die Abkürzung, den Titel,
        # den Vornamen und den Nachnamen des Arztes enthält.
        text += f"Birthdate: {doctor.get_birthdate()}; Age: {doctor.get_age()} \n"
        text += f"Profession: {doctor.get_profession()} \n"

        return text

    def display_blutbilder(self):
        text = ""
        blutbilder = self._model.get_Blutbilder() # Alle Blutbilder, die in dem Modell gespeichert sind, werden abgerufen.
        for blutbild in blutbilder: # Es wird eine Schleife über alle Blutbilder durchlaufen.
            text += f"ID: {blutbild.getPatID()}, Datum: {blutbild.getDate()} \n" # Für jedes Blutbild wird die Patienten-ID und das Datum hinzugefügt.
            text += f"Messwerte: {blutbild.getMesswerte()} \n" # Messwerte des Blutbilds werden hinzugefügt.

        return text
