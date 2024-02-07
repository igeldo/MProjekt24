class Activity(object):
    def __init__(self):
        self.getActivity()
        self.calcActivity(self.activityDays)

    def getActivity(self) -> int:
        while True:
            response = input("Do you have a physical job (Y/N)? ").strip().upper()
            if response == "Y":
                self.activityDays = 7
                return self.activityDays
            elif response == "N":
                break
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

        while True:
            response = input("Are you a professional athlete (Y/N)? ").strip().upper()
            if response == "Y":
                self.activityDays = 8
                return self.activityDays
            elif response == "N":
                break
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

        while True:
            try:
                activityDays = input("How many days per week do you practice sports? ")
                self.activityDays = int(activityDays)
                if 0 <= self.activityDays <= 7:
                    return self.activityDays
                else:
                    print("Please enter a valid number between 0 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calcActivity(self, activityDays) -> float:
        if activityDays == 0:
            self._sport = 1.2
            return self._sport
        elif activityDays == 1:
            self._sport = 1.375
            return self._sport
        elif activityDays == 2 or activityDays == 3:
            self._sport = 1.55
            return self._sport
        elif activityDays == 4 or activityDays == 5:
            self._sport = 1.725
            return self._sport
        elif activityDays == 6 or activityDays == 7:
            self._sport = 1.9
            return self._sport
        else:
            self._sport = 2.4
            return self._sport

    def getSport(self) -> float:
        return self._sport

