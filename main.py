from person import Person
from doctor import Doctor
from patient import Patient

class Main:
    def run(self):
        doctor1 = Doctor('Prof. Dr.', 'Maral', 'Safadi', '1970-09-06', '+4917765432109', 'MS', 'Internistin')
        doctor1.show_attributes()

        print('\n')

        patient1 = Patient('John', 'Doe', '1990-07-15','+4915123456789', 'JD', 'Keine', 'Fieber', 'Männlich')
        patient1.show_attributes()

        print('\n')

        patient2 = Patient('Jane', 'Smith', '1985-03-20','+4916234567890', 'JS',' Vorerkrankung am Herzen', 'Husten', 'Weiblich')
        patient2.show_attributes()

        print('\n')

        patient3 = Patient('Harald', 'Mueller', '1980-05-25', '+4917345678901', 'HM', 'Diabetes Typ II', 'Kopfschmerzen, Schwächegefühl', 'Männlich')
        patient3.show_attributes()

        print('\n')

        patient4 = Patient('Steffanie', 'Vogel', '1995-11-12', '+4918456789012', 'SV', 'Asthma', 'Atembeschwerden, Übelkeit', 'Weiblich')
        patient4.show_attributes()

if __name__ == '__main__':
    main = Main()
    main.run()
