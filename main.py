from Controller import Controller
from blutbild import Blutbild
from doctor import Doctor
from messwert import Messwert
from model import Model
from patient import Patient


class Main:
    def run(self):
        MainController = Controller()
        MainModel = Model()

        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', +4917765432109, 'MS', 'Internistin')
        MainModel.add_person(doctor1)

        patient1 = Patient('John', 'Doe', '1990-07-15', +4915123456789, 'JD', 'Keine', 'Fieber', 'Männlich')
        MainModel.add_person(patient1)
        blutbild1 = Blutbild('2024-04-06', 1)
        blutbild1.addMesswert(Messwert('HB', 9.0))
        blutbild1.addMesswert(Messwert('WBC', 6000))
        blutbild1.addMesswert(Messwert('RBC', 5.0))
        blutbild1.addMesswert(Messwert('PLT', 150000))

        MainModel.add_Blutbild(blutbild1)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', +4916234567890, 'JS', 'Vorerkrankung am Herzen', 'Husten',
                           'Weiblich')
        MainModel.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', +4917345678901, 'HM', 'Diabetes Typ II',
                           'Kopfschmerzen, Schwächegefühl', 'Männlich')
        MainModel.add_person(patient3)

        patient4 = Patient('Steffanie', 'Vogel', '1995-11-12', +4918456789012, 'SV', 'Asthma',
                           'Atembeschwerden, Übelkeit', 'Weiblich')
        MainModel.add_person(patient4)

        MainController.display_persons(MainModel)

        print(f"Blutbilder der Patienten:")
        print('\n')

        MainController.display_Blutbilder(MainModel)


if __name__ == '__main__':
    main = Main()
    main.run()
