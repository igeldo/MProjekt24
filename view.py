import matplotlib.pyplot as plt
import seaborn as sns

class HeartRateView:
    def __init__(self, model):
        self._model = model

    def plot_heart_rate(self):
        data=self._model.heart_rate_data
        plt.plot(data['Date'], data['HeartRate'])
        plt.xlabel('Date/Time')
        plt.ylabel('Heart Rate')
        plt.title('Heart Rate over Time')
        plt.show()


    def plot_correlation(self):
        data = self._model.heart_rate_data
        activity_mapping = {"Sleep": 0, "Wake up": 1, "Home": 2, "On the way": 3, "Appointment": 4, "Shower": 5,
                            "Breakfast": 6, "Get ready": 7, "Phone call": 8, "Meeting": 9, "Sport": 10, "Hiking": 11,
                            "Swimming": 12, "Clean up": 13, "Work": 14}
        data['Activity_Numeric'] = data['Activity'].map(activity_mapping)
        sns.scatterplot(data=data, x='HeartRate', y='Activity_Numeric')
        plt.title('Correlation between Heart Rate and Activity')
        plt.xlabel('Heart Rate')
        plt.ylabel('Activity')
        plt.yticks(list(activity_mapping.values()), list(activity_mapping.keys()))
        plt.show()