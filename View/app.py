from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout

from Controller import controllerGUI
from View.viewGUI import ViewGUI

# Hauptanwendungsklasse der App
class App(QWidget): # App erbt von der QWidget Klasse, die die Grundlage für grafische Benutzeroberflächen in Qt bildet.
    def __init__(self, controllergui: controllerGUI, view: ViewGUI):
        # controllergui: controllerGUI - Ein Objekt der controllerGUI Klasse,
        # das für die Steuerung und Verarbeitung der Anwendungslogik verantwortlich ist.

        # view: ViewGUI - Ein Objekt der ViewGUI Klasse,
        # das für die Darstellung der Benutzeroberfläche verantwortlich ist.
        super().__init__() # Der Konstruktor der Basisklasse QWidget wird aufgerufen, um die Initialisierung des Widgets sicherzustellen.
        self._title = 'Krankenhaus Verwaltung'
        self._controller = controllergui # Das übergebene controllergui Objekt wird in der App Klasse als _controller Attribut gespeichert.
        self._view = view
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self._title)
        #  Der Titel des Anwendungsfensters wird auf den zuvor in __init__() gesetzten Wert "Patienten-Verwaltung" gesetzt.

        # Hauptlayout
        main_layout = QHBoxLayout()

        # Layout für die Eingabefelder und Buttons
        left_layout = QVBoxLayout()

        self.label1 = QLabel('Patienten ID:', self)
        left_layout.addWidget(self.label1)

        self.entry1 = QLineEdit(self)
        left_layout.addWidget(self.entry1)

        self.label2 = QLabel('Aufnahmedatum (YYYY-MM-DD):', self)
        left_layout.addWidget(self.label2)

        self.entry2 = QLineEdit(self)
        left_layout.addWidget(self.entry2)

        self.label3 = QLabel('Messwert Typ:', self)
        left_layout.addWidget(self.label3)

        self.entry3 = QLineEdit(self)
        left_layout.addWidget(self.entry3)

        self.label4 = QLabel('Messwert Wert:', self)
        left_layout.addWidget(self.label4)

        self.entry4 = QLineEdit(self)
        left_layout.addWidget(self.entry4)

        self.addButton1 = QPushButton('Messwert speichern', self)
        self.addButton1.clicked.connect(self.handle_add_Messwert)
        left_layout.addWidget(self.addButton1)

        self.addButton2 = QPushButton('Blutbild hinzufügen', self)
        self.addButton2.clicked.connect(self.handle_add_blutbild) # Speichern der Patientendaten
        left_layout.addWidget(self.addButton2)

        self.displayButton = QPushButton('alle Daten anzeigen', self)
        self.displayButton.clicked.connect(self.handle_display_allData)
        left_layout.addWidget(self.displayButton)

        self.addButton3 = QPushButton('neue Person anlegen', self)
        self.addButton3.clicked.connect(self.handle_create_person)
        left_layout.addWidget(self.addButton3)

        right_layout = QHBoxLayout() # neues horizontales Layout

        self.resultLabel = QLabel('', self) # Der initiale Text des Labels ist leer ('').
        self.resultLabel.setWordWrap(True) # Aktiviert den Zeilenumbruch für den Text im resultLabel Widget.
        self.resultLabel.setStyleSheet("border: 1px solid black; padding: 10px;")  # Rahmen und Polsterung hinzufügen
        right_layout.addWidget(self.resultLabel)

        # Füge die beiden Layouts zum Hauptlayout hinzu
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Hauptlayout (main_layout) wird als das Layout der App Klasse gesetzt
        self.setLayout(main_layout)
        self.show()

    def handle_add_Messwert(self): # wird ausgeführt, wenn ein neuer Messwert hinzugefügt werden soll
        try:
            self._controller.add_Messwert(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Messwerts: {e}")

    def handle_add_blutbild(self): # wird ausgeführt, wenn ein neues Blutbild hinzugefügt werden soll
        try:
            self._controller.add_blutbild(self)
            self._view.display_allData(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Hinzufügen des Blutbilds: {e}")

    def handle_display_allData(self): # wird aufgerufen, um alle Daten in der Anwendung anzuzeigen
        try:
            self._view.display_allData(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Anzeigen aller Daten: {e}")

    def handle_create_person(self):
        try:
            self._controller.create_person(self)
        except Exception as e:
            self.show_error_message(f"Fehler beim Anlegen einer neuen Person: {e}")

    def show_error_message(self, message):
        QMessageBox.critical(self, 'Fehler', message)
        print(message)
