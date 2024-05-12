from Class_Person import Person
import pip as pip
from pip import openpyxl
pip install openpyx

class Main:
    def run(self):
        person1 = Person('Corinne', 28, 'female', 'good')
        person1.import_data('V0.1_HFdaten.xlsx') #Import von Exceldatei funktioniert noch nicht --> Frage!
        person1.analyze_heart_rate()

if __name__ == '__main__':
    main = Main()
    main.run()