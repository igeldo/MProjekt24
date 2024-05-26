import pandas as pd
from model import Person
from view import HeartRateView
import matplotlib.pyplot as plt

class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data = None

    def import_data(self, file_path):
        try:
            self.data = pd.read_excel(file_path)
            print(f"Data imported successfully from {file_path}")
        except Exception as e:
            print(f"Error importing data: {e}")

    def get_properties(self):
        return {
            'Name': self.model.name,
            'Age': self.model.age,
            'Sex': self.model.sex,
            'Fitness Level': self.model.fitness_level
        }

    def get_resting_heart_rate(self):
        return 60  # Placeholder for resting heart rate

    def get_maximum_heart_rate(self):
        return 180  # Placeholder for maximum heart rate

    def get_heart_rate_data_for_date(self, date):
        if self.data is not None:
            day_data = self.data[self.data['Date'] == date]
            return day_data
        return None

    def analyze_heart_rate(self):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['Date'], self.data['HeartRate'], label='Heart Rate')
            plt.xlabel('Date')
            plt.ylabel('Heart Rate (bpm)')
            plt.title('Heart Rate Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()

    def analyze_correlation(self):
        if self.data is not None:
            correlation_matrix = self.data.corr()
            print("Correlation Matrix:")
            print(correlation_matrix)

class HeartRateView:
    def __init__(self, model):
        self.model = model

    def display_properties(self, properties):
        print(f"Name: {properties['Name']}")
        print(f"Age: {properties['Age']}")
        print(f"Sex: {properties['Sex']}")
        print(f"Fitness Level: {properties['Fitness Level']}")

    def display_heart_rate(self, resting_heart_rate, max_heart_rate):
        print(f"Resting Heart Rate: {resting_heart_rate} bpm")
        print(f"Maximum Heart Rate: {max_heart_rate} bpm")

    def display_heart_rate_data_for_date(self, date, data):
        print(f"Heart Rate Data for {date}:")
        if data is not None and not data.empty:
            print(data)
        else:
            print("No data available for this date.")

    def display_heart_rate_analysis(self):
        print("Displaying heart rate analysis plot...")

    def display_correlation_analysis(self):
        print("Displaying correlation analysis...")


def analyze_correlation(self):
    if self.data is not None:
        # Exclude columns with datetime.time data type
        numeric_data = self.data.select_dtypes()

        if not numeric_data.empty:
            correlation_matrix = numeric_data.corr()
            print("Correlation Matrix:")
            print(correlation_matrix)
        else:
            print("No numeric data available for correlation analysis.")
