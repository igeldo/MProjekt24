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
            # lesen der Werte aus den Eingabefeldern
            patient_id = gui.entry1.text()
            pat_id = int(patient_id)
            aufnahmedatum = gui.entry2.text()

            # Überprüfung, ob Patienten-ID und das Aufnahmedatum tatsächlich eingegeben wurden
            if not (patient_id and aufnahmedatum):
                raise ValueError("Patienten ID und Aufnahmedatum müssen ausgefüllt sein.")

            self._blutbildneu.addPatID(pat_id)
            # Hier wird die addPatID()-Methode des _blutbildneu-Objekts aufgerufen, um die Patienten-ID hinzuzufügen.
            # Dadurch wird die Patienten-ID, die zuvor aus dem Eingabefeld gelesen wurde, in dem _blutbildneu-Objekt gespeichert.

            self._blutbildneu.addAufnahmedatum(date.fromisoformat(aufnahmedatum))

            self._model.add_Blutbild(self._blutbildneu)
            # Hier wird die add_Blutbild()-Methode des _model-Objekts aufgerufen,
            # um das aktualisierte _blutbildneu-Objekt dem Modell hinzuzufügen.

            self._model.linkBlutbildtoPatient(self._blutbildneu)
            # Beziehung zwischen dem Patienten und dem neuen Blutbild hergestellt.
            #            self._blutbildneu.clearAll()

            QMessageBox.information(gui, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.') # Informationsdialog angezeigt, um dem Benutzer mitzuteilen, dass das Blutbild erfolgreich hinzugefügt wurde.

            # Fehlerbehandlung
        except ValueError as e:
            QMessageBox.critical(gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_blutbild: {e}")

    def add_Messwert(self, gui):
        try: # auslesen aus den Eingabefeldern entry3 und entry4 des gui-Objekts
            messwert_type = gui.entry3.text()
            messwert_value = gui.entry4.text()
            messwert = float(messwert_value)

            if not (messwert_type and messwert_value):
                raise ValueError("Messwert Typ und Messwert Wert müssen ausgefüllt sein.")
            # Überprüfung, ob sowohl der Messwert-Typ als auch der Messwert-Wert eingegeben wurden

            # Wenn alles korrekt ist, wird der Messwert-Typ und der Messwert-Wert übergeben
            self._blutbildneu.addMesswert(Messwert(messwert_type, messwert))

            # Informationsdialog
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

    # neue Person erstellen
    def create_person(self, gui):
        self.person_app = PersonApp(self, self._view)
        # Sie erstellt ein Objekt der Klasse PersonApp und weist es der Variablen
        # self.person_app zu. Beim Erstellen des PersonApp-Objekts werden self
        # (also die aktuelle Instanz) und self._view als Parameter übergeben.
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

    # App starten
    def start(self):
        app = QApplication(sys.argv)
        ex = App(self, self._view)
        sys.exit(app.exec_())


