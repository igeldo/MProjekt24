import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time, date


class Person:
    def __init__(self, name, age, sex, fitness_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.fitness_level = fitness_level
        self.herz_rate_data = ()  # HF muss definiert werden um es zu improtieren zu können

    def import_data(self, excel_datei: str):
        df = pd.read_excel(excel_datei)
        data_list = df.to_dict(orient='records')
        return data_list

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

    def add_heart_rate_data(self, date, time, heart_rates):
        self.heart_rates[date] = heart_rates
        self.date = date
        self.time = time
        combine_datetime = datetime.combine(date, time)

    def analyze_heart_rate(self, combine_datetime, heart_rates):
        plt.plot(combine_datetime, heart_rates)  # Soll die Datum & Uhrzeit auf x-Achse plotten und die HF auf y Achse
        plt.xlabel('Date/Time')
        plt.ylabel('Heartrate')
        plt.title('heartfrequency')
        plt.show()
