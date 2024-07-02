import sys
from datetime import date

from PyQt5.QtWidgets import QMessageBox, QApplication

from Model.blutbild import Blutbild
from Model.messwert import Messwert
from Model.model import Model
from Model.patient import Patient
from View.app import App
from View.personApp import PersonApp


class ControllerGUI:
    def __init__(self, model: Model, view):
        self._model = model
        self._view = view

        self._blutbildneu = Blutbild(date(1999, 1, 1), 0)

    def add_blutbild(self, gui):
        try:
            patient_id = gui.entry1.text()
            pat_id = int(patient_id)
            aufnahmedatum = gui.entry2.text()

            if not (patient_id and aufnahmedatum):
                raise ValueError("Patienten ID und Aufnahmedatum müssen ausgefüllt sein.")

            self._blutbildneu.addPatID(pat_id)
            self._blutbildneu.addAufnahmedatum(date.fromisoformat(aufnahmedatum))
            self._model.add_Blutbild(self._blutbildneu)
            self._model.linkBlutbildtoPatient(self._blutbildneu)
            #            self._blutbildneu.clearAll()
            QMessageBox.information(gui, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.')
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_blutbild: {e}")

    def add_Messwert(self, gui):
        try:
            messwert_type = gui.entry3.text()
            messwert_value = gui.entry4.text()
            messwert = float(messwert_value)

            if not (messwert_type and messwert_value):
                raise ValueError("Messwert Typ und Messwert Wert müssen ausgefüllt sein.")

            self._blutbildneu.addMesswert(Messwert(messwert_type, messwert))
            QMessageBox.information(gui, 'Erfolg', 'Messwert erfolgreich gespeichert.')
            self.clear_Messwertentries(gui)
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_Messwert: {e}")

    def clear_Messwertentries(self, gui):
        gui.entry3.clear()
        gui.entry4.clear()

    def create_person(self, gui):
        self.person_app = PersonApp(self, self._view)
        self.person_app.show()



    def add_Patient(self, gui):
        try:
            name = gui.entry1.text()
            surname = gui.entry2.text()
            birth_date = gui.entry3.text()
            phonenumber = gui.entry4.text()
            phonenumber_int = int(phonenumber)
            abbreviation = gui.entry5.text()
            preillness = gui.entry6.text()
            symptoms = gui.entry7.text()
            sex = gui.entry8.text()
            patient = Patient(name, surname, birth_date, phonenumber_int, abbreviation, preillness, symptoms, sex)
            self._model.add_person(patient)
            QMessageBox.information(gui, 'Erfolg', 'Patient erfolgreich hinzugefügt.')
            self.person_app.close()
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_Patient: {e}")

    def start(self):
        app = QApplication(sys.argv)
        ex = App(self, self._view)
        sys.exit(app.exec_())


