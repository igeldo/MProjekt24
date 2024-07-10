from Controller.controller import Controller
from Controller.controllerGUI import ControllerGUI

from Model.exampleData import ExampleData
from Model.model import Model
from View.viewGUI import ViewGUI
from View.view import View


class Main:
    def run(self):
        main_model = Model()
        main_view = View(main_model)
        main_controller = Controller(main_model, main_view)
        gui_view = ViewGUI(main_model)
        gui_controller = ControllerGUI(main_model, gui_view)

        data = ExampleData(main_model)

        data.addDoctorData()
        data.addPatientData()
        data.addBlutbilderData()

        main_controller.start()
        gui_controller.start()


if __name__ == '__main__':
    main = Main()
    main.run()
