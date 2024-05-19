import matplotlib.pyplot as plt
import seaborn as sns


class HeartRateView:
    @staticmethod
    def plot_heart_rate(data):
        plt.plot(data['Date'], data['HeartRate'])
        plt.xlabel('Date/Time')
        plt.ylabel('Heartrate')
        plt.title('Heart Frequency')
        plt.show()

    def plot_correlation(self, data):
        sns.scatterplot(data=data, x='HeartRate', y='fitness_level')
        plt.title('Korrelation zwischen Herzfrequenz und Fitnesslevel')
        plt.xlabel('Herzfrequenz')
        plt.ylabel('Fitnesslevel')
        plt.show()