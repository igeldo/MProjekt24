from blutbildController import BlutbildController
from messwert import Messwert
from doctor import Doctor
from patient import Patient
from personController import PersonController
from blutbild import Blutbild


class Main:
    def run(self):
        controllerPerson = PersonController()
        controllerBlutbild = BlutbildController()

        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', '+4917765432109', 'MS', 'Internistin')
        controllerPerson.add_person(doctor1)

        patient1 = Patient('John', 'Doe', '1990-07-15', '+4915123456789', 'JD', 'Keine', 'Fieber', 'Männlich')
        controllerPerson.add_person(patient1)
        blutbild1 = Blutbild('2024-04-06', '1')
        blutbild1.addMesswert(Messwert('HB','9.0'))
        blutbild1.addMesswert(Messwert('WBC', '6000'))
        blutbild1.addMesswert(Messwert('RBC', '5.0'))
        blutbild1.addMesswert(Messwert('PLT', '150000'))

        controllerBlutbild.add_Blutbild(blutbild1)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', '+4916234567890', 'JS', 'Vorerkrankung am Herzen', 'Husten',
                           'Weiblich')
        controllerPerson.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', '+4917345678901', 'HM', 'Diabetes Typ II',
                           'Kopfschmerzen, Schwächegefühl', 'Männlich')
        controllerPerson.add_person(patient3)

        patient4 = Patient('Steffanie', 'Vogel', '1995-11-12', '+4918456789012', 'SV', 'Asthma',
                           'Atembeschwerden, Übelkeit', 'Weiblich')
        controllerPerson.add_person(patient4)

        controllerPerson.display_persons()

        print(f"Blutbilder der Patienten:")
        print('\n')

        controllerBlutbild.display_Blutbilder()


if __name__ == '__main__':
    main = Main()
    main.run()
