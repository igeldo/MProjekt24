from Controller.Controller import Controller
from Controller.ControllerGUI import ControllerGUI
from Model.exampleData import ExampleData
from Model.model import Model
from View.ViewGUI import ViewGUI
from View.view import View


class Main:
    def run(self):
        main_model = Model()
        main_view = View(main_model)
        main_controller = Controller(main_model, main_view)
        gui_view = ViewGUI(main_model)
        gui_controller = ControllerGUI(main_model, gui_view)

        Data = ExampleData(main_model)

        Data.addDoctorData()
        Data.addPatientData()
        Data.addBlutbilderData()

        main_controller.start()
        gui_controller.start()


if __name__ == '__main__':
    main = Main()
    main.run()
