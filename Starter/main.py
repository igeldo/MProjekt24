from Model.model import Person
from Controller.controller import PersonController
from View.view import HeartRateView

def main():
    #Inputrequests from User
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sex = input("Enter sex: ")
    fitness_level = input("Enter fitness level: ")

    model = Person(name, age, sex, fitness_level)
    view = HeartRateView(model)
    controller = PersonController(model, view)

    #Dataimport thrugh importrequest
    file_path = input("Enter the file path for data import: ").strip().replace('"', '').replace('\\', '/')
    controller.import_data(file_path)

    #Show information
    view.display_properties()
    view.display_heart_rate()

    #Call specific Heratratedata for selected Date
    specific_date = input("Enter a date for heart rate data (YYYY-MM-DD): ")
    day_data = controller.get_heart_rate_data_for_date(specific_date)
    view.display_heart_rate_data_for_date(specific_date, day_data)

    #Show specific Heartratedata for selected Date
    view.analyze_heart_rate(controller.data)
    controller.analyze_correlation()
    controller.calculate_mean_heart_rate_per_activity()

if __name__ == '__main__':
    main()