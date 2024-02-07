from datetime import datetime, date
from Activity import Activity
from Supply import Supply


class Person:
    def __init__(self):
        self._name = self.getName()
        self.getDateOfBirth()
        self.calcAge(self._dateOfBirth)
        self._weight = self.getWeight()
        self._height = self.getHeight()
        self._gender = self.getGender()
        self._supply = Supply()
        self._activity = Activity()

    def getName(self):
        name = input("What\'s your name? ")
        return name

    def getDateOfBirth(self):
        while True:
            try:
                dateOfBirthStr = input("What is your birth date (YYYY-MM-DD)? ")
                self._dateOfBirth = datetime.strptime(dateOfBirthStr, "%Y-%m-%d").date()
                self.calcAge(self._dateOfBirth)
                if 0 < self.age < 100:
                    break
                else:
                    print("Please enter a realistic date  (Year should be between " +
                          f"{date.today().year - 100} and {date.today().year}).")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def calcAge(self, dateOfBirth):
        today = date.today()
        daysInYear = 365.2425
        self.age = int((today - dateOfBirth).days / daysInYear)

    def getWeight(self):
        while True:
            try:
                weight = float(input("What is your weight in kg? "))
                if 10 <= weight <= 200:

                    return weight

                else:
                    print("Please enter a realistic weight (between 10 and 200 kg).")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def getHeight(self):
        while True:
            try:
                height = float(input("What is your height in cm? "))
                if 50 <= height <= 210:

                    return height

                else:
                    print("Please enter a realistic height (between 50 and 210 cm).")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def getGender(self):
        while True:
            gender = input("What is your gender (M,F)? ").strip().upper()
            if gender in ["M", "F"]:

                return gender

            else:
                print("Invalid input. Please enter 'M' for male or 'F' for female.")


    def calcBasalMetabolismHB(self) -> int:
        if self._gender == "M":
            HBM = 66.47 + (13.7 * self._weight) + (5 * self._height) - (6.8 * self.age)
            return HBM
        else:
            HBF = 655.1 + (9.6 * self._weight) + (1.8 * self._height) - (4.7 * self.age)
            return HBF

    def calcBasalMetabolismMSJ(self) -> int:
        if self._gender == "M":
            MSJM = (10 * self._weight) + (6.25 * self._height) - (5 * self.age) + 5
            return MSJM
        else:
            MSJF = (10 * self._weight) + (6.25 * self._height) - (5 * self.age) - 161
            return MSJF

    def calcBasalMetabolismS(self) -> int:
        if self._gender == "M":
            if self.age < 3:
                simpleM = 59.512 * self._weight - 30.4
            elif self.age < 10:
                simpleM = 22.706 * self._weight + 504.3
            elif self.age < 18:
                simpleM = 22.706 * self._weight + 658.2
            elif self.age < 30:
                simpleM = 15.057 * self._weight + 692.2
            elif self.age < 60:
                simpleM = 11.472 * self._weight + 873.1
            else:
                simpleM = 11.711 * self._weight + 587.7
            return simpleM
        else:
            if self.age < 3:
                simpleF = 58.317 * self._weight - 31.1
            elif self.age < 10:
                simpleF = 20.315 * self._weight + 485.9
            elif self.age < 18:
                simpleF = 13.384 * self._weight + 692.6
            elif self.age < 30:
                simpleF = 14.818 * self._weight + 486.6
            elif self.age < 60:
                simpleF = 8.126 * self._weight + 845.6
            else:
                simpleF = 9.082 * self._weight + 658.5
            return simpleF

    def print(self):
        print(f" Name: ", self._name)
        print(f" Age: ", self.age)
        print(f" Weight: ", self._weight)
        print(f" Height: ", self._height)
        print(f" Gender: ", self._gender)
        print(f" Calculated supply: ", self._supply.calcTotalCalories())
        print(f" Basal Metabolism HB: ", self.calcBasalMetabolismHB())
        print(f" Basal Metabolism MSJ: ", self.calcBasalMetabolismMSJ())
        print(f" Basal Metabolism S: ", self.calcBasalMetabolismS())
        totalMetabolismHB = self._supply.calcTotalCalories() - (
                    self.calcBasalMetabolismHB() * self._activity.getSport())
        print(f" Total Metabolism HB: ", totalMetabolismHB)
        totalMetabolismMSJ = self._supply.calcTotalCalories() - (
                self.calcBasalMetabolismMSJ() * self._activity.getSport())
        print(f" Total Metabolism MSJ: ", totalMetabolismMSJ)
        totalMetabolismS = self._supply.calcTotalCalories() - (
                self.calcBasalMetabolismS() * self._activity.getSport())
        print(f" Total Metabolism S: ", totalMetabolismS)
