from doctor import Doctor
from patient import Patient
from personController import PersonController

class Main:
    def run(self):
        controller = PersonController()

        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', '+4917765432109', 'MS', 'Internistin')
        controller.add_person(doctor1)

        patient1 = Patient('John', 'Doe', '1990-07-15', '+4915123456789', 'JD', 'Keine', 'Fieber', 'Männlich')
        controller.add_person(patient1)

        patient2 = Patient('Jane', 'Smith', '1985-03-20', '+4916234567890', 'JS', 'Vorerkrankung am Herzen', 'Husten', 'Weiblich')
        controller.add_person(patient2)

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', '+4917345678901', 'HM', 'Diabetes Typ II', 'Kopfschmerzen, Schwächegefühl', 'Männlich')
        controller.add_person(patient3)

        patient4 = Patient('Steffanie', 'Vogel', '1995-11-12', '+4918456789012', 'SV', 'Asthma', 'Atembeschwerden, Übelkeit', 'Weiblich')
        controller.add_person(patient4)

        controller.display_persons()

if __name__ == '__main__':
    main = Main()
    main.run()
