"""Importieren der Bibliotheken"""
import os
import pandas as pd
import matplotlib.pyplot as plt




class Person:
    def __init__(self, vorname, alter, geschlecht, fitness_level):
        self.vorname = vorname
        self.alter = alter
        self.geschlecht = geschlecht
        self.fitness_level = fitness_level
        self.herz_rate_data = () #HF muss definiert werden um es zu improtieren zu können

    def Daten_Importieren (cls, excel_datei):
        df = pd.read_excel(excel_datei)
        data_list = df.to_dict(orient='records')
        return data_list

    def Ruheherzfrequenz:
# Definition der RuheHF für Geschlecht nach Alter und Fitnesslevel


    def Maximalherfrequenz: #Definition der maximalen HF nach Standadformel 220-Alter


    def add_heart_rate_data(self, date, time, heart_rates):
        self.heart_rate_data[date] = heart_rates
        self.date = date
        self.time = time
        combine_datetime = datetime.combine(date, time)


    def Analyse_Herzfrequenz:
        plt.plot(combine_datetime, hear_rate_data)  # Soll die Datum & Uhrzeit auf x-Achse plotten und die HF auf y Achse
        plt.xlabel('Datum/Uhrzeit')
        plt.ylabel('Herzfrequenz')
        plt.title('Herzfrequenzdaten')
        plt.show()

person1 = Person('Corinne', 28, 'weiblich', 'durchschnitt')
person1.Daten_Importieren('v0.1_HFdaten')
person1.Analyse_Herzfrequenz()