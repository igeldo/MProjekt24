import sys

from PyQt5.QtWidgets import QApplication

from Controller.ControllerGUI import ControllerGUI
from View.ViewGUI import ViewGUI
from View.app import App
from Controller import Controller
from Model.blutbild import Blutbild
from Model.doctor import Doctor
from Model.messwert import Messwert
from Model.model import Model
from Model.patient import Patient
from View.view import View


class Main:
    def run(self):
        MainModel = Model()
        MainView = View(MainModel)
        MainController = Controller(MainModel, MainView)
        GUIView = ViewGUI(MainModel)
        GUIController = ControllerGUI(MainModel, GUIView)


        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', +4917765432109, 'MS', 'Internistin')
        MainModel.add_person(doctor1)

        patient1 = Patient('John', 'Doe', '1990-07-15', +4915123456789, 'JD', 'Keine', 'Fieber', 'Männlich')
        MainModel.add_person(patient1)
        blutbild1 = Blutbild('2024-04-02', 1)
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))

        MainModel.add_Blutbild(blutbild1)
        MainModel.linkBlutbildtoPatient(patient1, blutbild1)

        blutbild2 = Blutbild('2024-04-06', 1)
        blutbild2.addMesswert(Messwert('HB', 9.5))
        blutbild2.addMesswert(Messwert('WBC', 8000))
        blutbild2.addMesswert(Messwert('RBC', 6.0))
        blutbild2.addMesswert(Messwert('PLT', 300000))

        MainModel.add_Blutbild(blutbild2)
        MainModel.linkBlutbildtoPatient(patient1, blutbild2)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', +4916234567890, 'JS', 'Vorerkrankung am Herzen', 'Husten',
                           'Weiblich')
        MainModel.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', +4917345678901, 'HM', 'Diabetes Typ II',
                           'Kopfschmerzen, Schwächegefühl', 'Männlich')
        MainModel.add_person(patient3)

        patient4 = Patient('Steffanie', 'Vogel', '1995-11-12', +4918456789012, 'SV', 'Asthma',
                           'Atembeschwerden, Übelkeit', 'Weiblich')
        MainModel.add_person(patient4)

        MainController.start()



if __name__ == '__main__':
    main = Main()
    main.run()
    app = QApplication(sys.argv)
    ex = App(ControllerGUI, ViewGUI)
    sys.exit(app.exec_())
