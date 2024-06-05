from model import Person
from controller import PersonController
from view import HeartRateView

def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sex = input("Enter sex: ")
    fitness_level = input("Enter fitness level: ")

    model = Person(name, age, sex, fitness_level)
    view = HeartRateView(model)
    controller = PersonController(model, view)

    file_path = input("Enter the file path for data import: ").strip().replace('"', '').replace('\\', '/')
    controller.import_data(file_path)
    view.display_properties()

    resting_heart_rate = controller.get_resting_heart_rate()
    max_heart_rate = controller.get_maximum_heart_rate()
    view.display_heart_rate(resting_heart_rate, max_heart_rate)

    specific_date = input("Enter a date for heart rate data (YYYY-MM-DD): ")
    day_data = controller.get_heart_rate_data_for_date(specific_date)
    view.display_heart_rate_data_for_date(specific_date, day_data)

    view.analyze_heart_rate(controller.data)
    controller.analyze_correlation()
    controller.calculate_mean_heart_rate_per_activity()

if __name__ == '__main__':
    main()