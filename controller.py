import numpy
import numpy as np
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
        if self.model.sex == 'male':
            if self.model.age < 30:
                if self.model.fitness_level == 'excelent':
                    return 65
                elif self.model.fitness_level == 'good':
                    return 68
                elif self.model.fitness_level == 'low':
                    return 72
            elif 30 <= self.model.age < 50:
                if self.model.fitness_level == 'excelent':
                    return 67
                elif self.model.fitness_level == 'good':
                    return 70
                elif self.model.fitness_level == 'low':
                    return 74
            elif self.model.age >= 50:
                if self.model.fitness_level == 'excelent':
                    return 70
                elif self.model.fitness_level == 'good':
                    return 72
                elif self.model.fitness_level == 'low':
                    return 76
        elif self.model.sex == 'female':
            if self.model.age < 30:
                if self.model.fitness_level == 'excelent':
                    return 68
                elif self.model.fitness_level == 'good':
                    return 71
                elif self.model.fitness_level == 'low':
                    return 75
            elif 30 <= self.model.age < 50:
                if self.model.fitness_level == 'excelent':
                    return 70
                elif self.model.fitness_level == 'good':
                    return 73
                elif self.model.fitness_level == 'low':
                    return 77
            elif self.model.age >= 50:
                if self.model.fitness_level == 'excelent':
                    return 73
                elif self.model.fitness_level == 'good':
                    return 76
                elif self.model.fitness_level == 'low':
                    return 80

    def get_maximum_heart_rate(self):
        return 220-self.model.age

    def get_heart_rate_data_for_date(self, date):
        if self.data is not None:
            day_data = self.data[self.data['Date'] == date]
            return day_data
        return None

    def analyze_correlation(self):
        if self.data is not None:#
            x = np.array (['Sleep','Sleep','Sleep','Busy','Phone','Busy','Busy'])
            y = np.array ([80, 82, 84, 130, 120, 110, 115])
            plt.scatter(x,y)
            plt.show()
            x1 = self.data['Activity'].to_numpy(dtype='U')
            y1 = self.data['HeartRate'].to_numpy()
            plt.scatter(x1, y1)
            plt.show()
            #matrix = np.array ([1, 1, 1, 2, 2, 2],[80, 82, 84, 120, 110, 115])
            #result = np.correlate([1, 1, 1, 2, 2, 2], [80, 82, 84, 120, 110, 115])
            #result = numpy.correlate(self.data['Activity'], self.data['HeartRate'])
            #correlation_matrix = self.data.corr()
            #print("Correlation Matrix:")
            #print(correlation_matrix)

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
