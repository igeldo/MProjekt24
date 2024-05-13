from person import Person
from doctor import Doctor

class Main:
    def run(self):
        person1 = Person('Harald', 'Mueller', '1980-05-25', 'HM')
        person1.show_attributes()

        print('\n')

        person2 = Person('Steffanie', 'Vogel', '1995-11-12', 'SV')
        person2.show_attributes()

        print('\n')

        doctor1 = Doctor('Maral', 'Safadi', '1970-09-06', 'MS', 'Internistin')
        doctor1.show_attributes()

if __name__ == '__main__':
    main = Main()
    main.run()
