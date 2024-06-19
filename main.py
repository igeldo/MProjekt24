import sys

from PyQt5.QtWidgets import QApplication

from Controller.Controller import Controller
from Controller.ControllerGUI import ControllerGUI

from Model.doctor import Doctor
from Model.model import Model

from View.ViewGUI import ViewGUI


from Model.blutbild import Blutbild

from Model.messwert import Messwert

from Model.patient import Patient
from View.app import App

from View.view import View


class Main:
    def run(self):
        main_model = Model()
        main_view = View(main_model)
        main_controller = Controller(main_model, main_view)

        app = QApplication(sys.argv)
        gui_view = ViewGUI(main_model)
        gui_controller = ControllerGUI(main_model, gui_view)
        ex = App(gui_controller, gui_view)


        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', +4917765432109, 'MS', 'Internistin')
        main_model.add_person(doctor1)

        patient1 = Patient('John', 'Doe', '1990-07-15', +4915123456789, 'JD', 'Keine', 'Fieber', 'Männlich')
        main_model.add_person(patient1)
        blutbild1 = Blutbild('2024-04-02', 1)
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))

        main_model.add_Blutbild(blutbild1)
        main_model.linkBlutbildtoPatient(blutbild1)

        blutbild2 = Blutbild('2024-04-06', 1)
        blutbild2.addMesswert(Messwert('HB', 9.5))
        blutbild2.addMesswert(Messwert('WBC', 8000))
        blutbild2.addMesswert(Messwert('RBC', 6.0))
        blutbild2.addMesswert(Messwert('PLT', 300000))

        main_model.add_Blutbild(blutbild2)
        main_model.linkBlutbildtoPatient(blutbild2)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', +4916234567890, 'JS', 'Vorerkrankung am Herzen', 'Husten',
                           'Weiblich')
        main_model.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', +4917345678901, 'HM', 'Diabetes Typ II',
                           'Kopfschmerzen, Schwächegefühl', 'Männlich')
        main_model.add_person(patient3)


        main_controller.start()


        sys.exit(app.exec_())



if __name__ == '__main__':
    main = Main()
    main.run()

