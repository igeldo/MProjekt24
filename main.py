import datetime
from person import Person


class Main:
    def run(self):
        person1 = Person('Harald', 'Mueller', datetime.date(1972, 5, 12), 'HM')
        person1.show_attributes()
        person2 = Person('Steffanie', 'Vogel', 'xxx', 'SV')
        person2.show_attributes()


if __name__ == '__main__':
    main = Main()
    main.run()
