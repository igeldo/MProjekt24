from View import app


class ControllerGUI:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._gui = app.App

    def add_blutbild(self):
        patient_id = self._gui.entry1.text()
        aufnahmedatum = self._gui.entry2.text()

        if not (patient_id and aufnahmedatum ):
            self._gui.QMessageBox.critical(self, 'Fehler', 'Patienten ID und Aufnahmedatum müssen ausgefüllt sein.')
            return

        try:
            self._blutbildneu.addPatID(patient_id)
            self._blutbildneu.addAufnahmedatum(aufnahmedatum)
            self._model.add_Blutbild(self._blutbildneu)
            self._blutbildneu.clearAll()
            self._gui.QMessageBox.information(self, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.')
            # self.clear_entries()
        except ValueError as e:
            self._gui.QMessageBox.critical(self, 'Fehler', f'Fehler bei der Eingabe: {e}')

    def add_Messwert(self):
        messwert_type = self.entry3.text()
        messwert_value = self.entry4.text()

        if not (messwert_type and messwert_value):
            self._gui.QMessageBox.critical(self, 'Fehler', 'Messwert Typ und Messwert Wert müssen ausgefüllt sein.')
            return

        try:
            self._blutbildneu.addMesswert(Messwert(messwert_type, float(messwert_value)))
            self._gui.QMessageBox.information(self, 'Erfolg', 'Messwert erfolgreich gespeichert.')
            self.clear_Messwertentries()
        except ValueError as e:
            self._gui.QMessageBox.critical(self, 'Fehler', f'Fehler bei der Eingabe: {e}')

    def clear_allentries(self):
        self._gui.entry1.clear()
        self._gui.entry2.clear()
        self._gui.entry3.clear()
        self._gui.entry4.clear()

    def clear_Messwertentries(self):
        self._gui.entry3.clear()
        self._gui.entry4.clear()