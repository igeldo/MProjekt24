import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

# Importiere hier die notwendigen Klassen und initialisiere das Modell und den Controller
from Model.blutbild import Blutbild
from messwert import Messwert
from blutbildController import BlutbildController

controller = BlutbildController()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Krankenhaus Verwaltung'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.layout = QVBoxLayout()

        self.label1 = QLabel('Patienten ID:', self)
        self.layout.addWidget(self.label1)

        self.entry1 = QLineEdit(self)
        self.layout.addWidget(self.entry1)

        self.label2 = QLabel('Aufnahmedatum (YYYY-MM-DD):', self)
        self.layout.addWidget(self.label2)

        self.entry2 = QLineEdit(self)
        self.layout.addWidget(self.entry2)

        self.label3 = QLabel('Messwert Typ:', self)
        self.layout.addWidget(self.label3)

        self.entry3 = QLineEdit(self)
        self.layout.addWidget(self.entry3)

        self.label4 = QLabel('Messwert Wert:', self)
        self.layout.addWidget(self.label4)

        self.entry4 = QLineEdit(self)
        self.layout.addWidget(self.entry4)

        self.addButton = QPushButton('Blutbild hinzufügen', self)
        self.addButton.clicked.connect(self.add_blutbild)
        self.layout.addWidget(self.addButton)

        self.displayButton = QPushButton('Blutbilder anzeigen', self)
        self.displayButton.clicked.connect(self.display_blutbilder)
        self.layout.addWidget(self.displayButton)

        self.resultLabel = QLabel('', self)
        self.resultLabel.setWordWrap(True)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)
        self.show()

    def add_blutbild(self):
        patient_id = self.entry1.text()
        aufnahmedatum = self.entry2.text()
        messwert_type = self.entry3.text()
        messwert_value = self.entry4.text()

        if not (patient_id and aufnahmedatum and messwert_type and messwert_value):
            QMessageBox.critical(self, 'Fehler', 'Alle Felder müssen ausgefüllt werden.')
            return

        try:
            blutbild = Blutbild(aufnahmedatum, int(patient_id))
            blutbild.addMesswert(Messwert(messwert_type, float(messwert_value)))
            controller.add_Blutbild(blutbild)
            QMessageBox.information(self, 'Erfolg', 'Blutbild erfolgreich hinzugefügt.')
            self.clear_entries()
        except ValueError as e:
            QMessageBox.critical(self, 'Fehler', f'Fehler bei der Eingabe: {e}')

    def display_blutbilder(self):
        blutbilder = controller.Blutbilder
        result_text = ""
        for blutbild in blutbilder:
            result_text += f"Patienten ID: {blutbild.getPatID()}, Aufnahmedatum: {blutbild.getDate()}, Messwerte: {blutbild.getMesswerte()}\n"
        self.resultLabel.setText(result_text)

    def clear_entries(self):
        self.entry1.clear()
        self.entry2.clear()
        self.entry3.clear()
        self.entry4.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
