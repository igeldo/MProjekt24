from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout
from Controller import controllerGUI

from View.viewGUI import ViewGUI

# nach dem betätigen des Buttons 'neue Person anlegen' soll ein neues Fenster geöffnet werden
# und es soll neue Patienten aufgenommen werden

class PersonApp(QWidget):
    def __init__(self, controllergui: controllerGUI, view: ViewGUI):
        # controllergui: Eine Instanz der controllerGUI-Klasse, die die Steuerungslogik der Anwendung enthält.
        # view: Eine Instanz der ViewGUI-Klasse, die für die Darstellung der Benutzeroberfläche verantwortlich ist.
        super().__init__() # Der Konstruktor der Basisklasse QWidget wird aufgerufen, um das Widget zu initialisieren.
        self._title = 'Patienten-Verwaltung' # Titel
        self._controller = controllergui # Eine Referenz auf die controllerGUI-Instanz wird in der Klasse gespeichert.
        self._view = view # Eine Referenz auf die ViewGUI-Instanz wird in der Klasse gespeichert.
        self.initUI() # Benutzeroberfläche initialisieren

    # Benutzeroberfläche:
    def initUI(self):
        self.setWindowTitle(self._title)
    #  Der Titel des Anwendungsfensters wird auf den zuvor in __init__() gesetzten Wert "Patienten-Verwaltung" gesetzt.

        # Hauptlayout
        main_layout = QHBoxLayout() # horizontales Layout

        # Layout für die Eingabefelder und Buttons
        left_layout = QVBoxLayout()

        # Beschriftungen und Eingabefelder für verschiedene Patientendaten
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

        self.addButton1 = QPushButton('Save Patient Data', self) # Button "Save Patient Data" wird erstellt
        self.addButton1.clicked.connect(self.handle_add_patient) # Speichern der Patientendaten
        left_layout.addWidget(self.addButton1)


        main_layout.addLayout(left_layout) # Das left_layout mit den Eingabefeldern und dem Button wird dem main_layout hinzugefügt.

        self.setLayout(main_layout) # Das main_layout wird als Layout für das PersonApp-Widget gesetzt.
        self.show() # Das PersonApp-Widget wird angezeigt.

    # Verarbeitung des Speichervorgangs von Patientendaten
    def handle_add_patient(self): # Diese Methode wird aufgerufen, wenn der Benutzer den "Save Patient Data"-Button klickt.
        try:
            self._controller.add_Patient(self) # Patientendaten werden mithilfe der add_Patient(self) Methode des _controller Objekts gespeichert.
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Patienten: {e}")

    def show_error_message(self, message): # nimmt eine Fehlermeldung als Parameter entgegen
        QMessageBox.critical(self, 'Fehler', message) # Sie erstellt ein QMessageBox-Objekt, um die Fehlermeldung in einem Dialog-Fenster anzuzeigen
        print(message) #  Fehlermeldung auch in der Konsole angezeigt
