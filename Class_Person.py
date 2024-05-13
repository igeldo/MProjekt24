import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time, date


class Person:
    def __init__(self, name, age, sex, fitness_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.fitness_level = fitness_level
        self.heart_rate_data = ()  # HF muss definiert werden um es zu improtieren zu können

    def import_data(self, excel_datei: str):
        df = pd.read_excel(excel_datei)
        self.heart_rate_data = df
        return self.heart_rate_data

    def resting_heart_rate(self):  # Definition der RuheHF für Geschlecht nach Alter und Fitnesslevel
        if self.sex == 'male':
            if self.age <= 25:
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 69
                elif self.fitness_level == 'low':
                    return 81
            elif 25 < self.age <= 35:
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 70
                elif self.fitness_level == 'low':
                    return 81
            elif 35 < self.age <= 45:
                if self.fitness_level == 'excellent':
                    return 62
                elif self.fitness_level == 'good':
                    return 70
                elif self.fitness_level == 'low':
                    return 82
            elif 45 < self.age <= 55:
                if self.fitness_level == 'excellent':
                    return 63
                elif self.fitness_level == 'good':
                    return 71
                elif self.fitness_level == 'low':
                    return 83
            elif 55 < self.age >= 65:  # wie angeben alter 56+??
                if self.fitness_level == 'excellent':
                    return 61
                elif self.fitness_level == 'good':
                    return 67
                elif self.fitness_level == 'low':
                    return 81
        elif self.sex == 'female':
            if self.age <= 25:
                if self.fitness_level == 'excellent':
                    return 65
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 84
            elif 25 < self.age <= 35:
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 72
                elif self.fitness_level == 'low':
                    return 82
            elif 35 < self.age <= 45:
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 84
            elif 45 < self.age <= 55:
                if self.fitness_level == 'excellent':
                    return 65
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 83
            elif 55 < self.age >= 65:  # wie angeben alter 56+??
                if self.fitness_level == 'excellent':
                    return 64
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 83

    def maximum_heart_rate(self, maximum_hear_rate):  # Definition der maximalen HF nach Standadformel 220-Alter
        self.maximum_hear_rate = maximum_hear_rate
        maximum_hear_rate = 220 - self.age
        return maximum_hear_rate

    def add_heart_rate_data(self, date, time, heart_rate_data):
        self.heart_rate_data[date] = heart_rate_data
        self.date = date
        self.time = time
        combine_datetime = datetime.combine(date, time)

    def analyze_heart_rate(self, combine_datetime=None, heart_rates=None):
        plt.plot(self.heart_rate_data['Date'],self.heart_rate_data['HeartRate'])  # Soll die Datum & Uhrzeit auf x-Achse plotten und die HF auf y Achse
        plt.xlabel('Date/Time')
        plt.ylabel('Heartrate')
        plt.title('heartfrequency')
        plt.show()
