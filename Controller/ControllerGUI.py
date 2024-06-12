from datetime import date
from PyQt5.QtWidgets import QMessageBox

from Model.blutbild import Blutbild
from Model.messwert import Messwert


class ControllerGUI:
    def __init__(self, model, view, gui):
        self._model = model
        self._view = view
        self._gui = gui
        self._blutbildneu = Blutbild(None, None)

    def add_blutbild(self):
        try:
            patient_id = self._gui.entry1.text()
            aufnahmedatum = self._gui.entry2.text()

            if not (patient_id and aufnahmedatum):
                raise ValueError("Patienten ID und Aufnahmedatum müssen ausgefüllt sein.")

            self._blutbildneu.addPatID(patient_id)
            self._blutbildneu.addAufnahmedatum(date.fromisoformat(aufnahmedatum))
            self._model.add_Blutbild(self._blutbildneu)
            self._blutbildneu.clearAll()
            QMessageBox.information(self._gui, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.')
        except ValueError as e:
            QMessageBox.critical(self._gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(self._gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_blutbild: {e}")

    def add_Messwert(self):
        try:
            messwert_type = self._gui.entry3.text()
            messwert_value = self._gui.entry4.text()

            if not (messwert_type and messwert_value):
                raise ValueError("Messwert Typ und Messwert Wert müssen ausgefüllt sein.")

            self._blutbildneu.addMesswert(Messwert(messwert_type, float(messwert_value)))
            QMessageBox.information(self._gui, 'Erfolg', 'Messwert erfolgreich gespeichert.')
            self.clear_Messwertentries()
        except ValueError as e:
            QMessageBox.critical(self._gui, 'Fehler', f'Fehler bei der Eingabe: {e}')
        except Exception as e:
            QMessageBox.critical(self._gui, 'Fehler', f'Unerwarteter Fehler: {e}')
            print(f"Fehler in add_Messwert: {e}")

    def clear_Messwertentries(self):
        self._gui.entry3.clear()
        self._gui.entry4.clear()