from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout
from Controller import controllerGUI

from View.viewGUI import ViewGUI


class PersonApp(QWidget):
    def __init__(self, controllergui: controllerGUI, view: ViewGUI):
        super().__init__()
        self._title = 'Patienten-Verwaltung'
        self._controller = controllergui
        self._view = view
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self._title)

        # Hauptlayout
        main_layout = QHBoxLayout()

        # Layout für die Eingabefelder und Buttons
        left_layout = QVBoxLayout()

        self.label1 = QLabel('Name:', self)
        left_layout.addWidget(self.label1)

        self.entry1 = QLineEdit(self)
        left_layout.addWidget(self.entry1)

        self.label2 = QLabel('Surname:', self)
        left_layout.addWidget(self.label2)

        self.entry2 = QLineEdit(self)
        left_layout.addWidget(self.entry2)

        self.label3 = QLabel('Birthdate (YYYY-MM-DD):', self)
        left_layout.addWidget(self.label3)

        self.entry3 = QLineEdit(self)
        left_layout.addWidget(self.entry3)

        self.label4 = QLabel('Phone Number:', self)
        left_layout.addWidget(self.label4)

        self.entry4 = QLineEdit(self)
        left_layout.addWidget(self.entry4)

        self.label5 = QLabel('Abbreviation:', self)
        left_layout.addWidget(self.label5)

        self.entry5 = QLineEdit(self)
        left_layout.addWidget(self.entry5)

        self.label6 = QLabel('PreIllness:', self)
        left_layout.addWidget(self.label6)

        self.entry6 = QLineEdit(self)
        left_layout.addWidget(self.entry6)

        self.label7 = QLabel('Symptoms:', self)
        left_layout.addWidget(self.label7)

        self.entry7 = QLineEdit(self)
        left_layout.addWidget(self.entry7)

        self.label8 = QLabel('Sex:', self)
        left_layout.addWidget(self.label8)

        self.entry8 = QLineEdit(self)
        left_layout.addWidget(self.entry8)

        self.addButton1 = QPushButton('Save Patient Data', self)
        self.addButton1.clicked.connect(self.handle_add_patient)
        left_layout.addWidget(self.addButton1)


        main_layout.addLayout(left_layout)

        self.setLayout(main_layout)
        self.show()

    def handle_add_patient(self):
        try:
            self._controller.add_Patient(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Patienten: {e}")

    def show_error_message(self, message):
        QMessageBox.critical(self, 'Fehler', message)
        print(message)
