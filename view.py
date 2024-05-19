import matplotlib.pyplot as plt

class HeartRateView:
    @staticmethod
    def plot_heart_rate(data):
        plt.plot(data['Date'], data['HeartRate'])
        plt.xlabel('Date/Time')
        plt.ylabel('Heartrate')
        plt.title('Heart Frequency')
        plt.show()