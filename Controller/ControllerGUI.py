from datetime import date
from PyQt5.QtWidgets import QMessageBox

from Model.blutbild import Blutbild
from Model.messwert import Messwert
from Model.model import Model


class ControllerGUI:
    def __init__(self, model: Model, view):
        self._model = model
        self._view = view

        self._blutbildneu = Blutbild(0000-00-00, 0)

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
