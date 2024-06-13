import sys

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QWidget

from Controller import ControllerGUI
from Model.model import Model
from View.ViewGUI import ViewGUI


class App(QWidget):
    def __init__(self, controllergui: ControllerGUI, view: ViewGUI):
        super().__init__()
        self._title = 'Krankenhaus Verwaltung'
        self._controller = controllergui
        self._view = view
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self._title)

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

        self.addButton1 = QPushButton('Messwert speichern', self)
        self.addButton1.clicked.connect(self.handle_add_Messwert)
        self.layout.addWidget(self.addButton1)

        self.addButton2 = QPushButton('Blutbild hinzufügen', self)
        self.addButton2.clicked.connect(self.handle_add_blutbild)
        self.layout.addWidget(self.addButton2)

        self.displayButton = QPushButton('alle Daten anzeigen', self)
        self.displayButton.clicked.connect(self.handle_display_allData)
        self.layout.addWidget(self.displayButton)

        self.resultLabel = QLabel('', self)
        self.resultLabel.setWordWrap(True)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)
        self.show()

    def handle_add_Messwert(self):
        try:
            self._controller.add_Messwert(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Messwerts: {e}")

    def handle_add_blutbild(self):
        try:
            self._controller.add_blutbild(self)
            self._view.display_allData(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Blutbilds: {e}")

    def handle_display_allData(self):
        try:
            self._view.display_allData(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Anzeigen aller Daten: {e}")

    def show_error_message(self, message):
        QMessageBox.critical(self, 'Fehler', message)
        print(message)


