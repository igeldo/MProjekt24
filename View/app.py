from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from Controller import ControllerGUI
import ViewGUI


# Importiere hier die notwendigen Klassen und initialisiere das Modell und den Controller


class App(QWidget):
    def __init__(self, controller: ControllerGUI, view: ViewGUI):
        super().__init__()
        self._title = 'Krankenhaus Verwaltung'
        self._controller = controller
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

        self.addButton = QPushButton('Messwert speichern', self)
        self.addButton.clicked.connect(self._controller.add_Messwert)
        self.layout.addWidget(self.addButton)

        self.addButton = QPushButton('Blutbild hinzufügen', self)
        self.addButton.clicked.connect(self._controller.add_blutbild)
        self.layout.addWidget(self.addButton)

        self.displayButton = QPushButton('Blutbilder anzeigen', self)
        self.displayButton.clicked.connect(self._view.display_allData)
        self.layout.addWidget(self.displayButton)

        self.resultLabel = QLabel('', self)
        self.resultLabel.setWordWrap(True)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)
        self.show()

