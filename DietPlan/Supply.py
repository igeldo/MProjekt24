class Supply(object):
    def __init__(self):
        self.foodList = []
        self.getFood()
        self.calcCalories()
        self.showInfo()
        self._totalCalories = self.calcTotalCalories()

    def getFood(self):
        while True:
            self.name = input("Enter the name of the food: ")
            while True:
                try:
                    self.gram = float(input("Enter the amount of grams eaten: "))
                    if self.gram >= 0:
                        break
                    else:
                        print("Please enter a non-negative number for grams.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    self.caloriesPer100g = float(input("Enter the calories per 100g: "))
                    if self.caloriesPer100g >= 0:
                        break
                    else:
                        print("Please enter a non-negative number for calories per 100g.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            self.foodList.append((self.name, self.gram, self.caloriesPer100g))

            print(self.showInfo())

            while True:
                add_food = input("Would you like to add another food? ('Y' for yes or 'N' for no): ")
                if add_food.upper() == 'Y':
                    break
                elif add_food.upper() == 'N':
                    return self.foodList
                else:
                    print(
                        "Invalid input. Please enter 'Y' for yes or 'N' for no.")

    def calcCalories(self) -> float:
        return (self.gram / 100) * self.caloriesPer100g

    def showInfo(self):
        return f"{self.name}: {self.gram}g, {self.caloriesPer100g} Kcal/100g, Total: {self.calcCalories()} Kcal"

    def calcTotalCalories(self):
        totalCalories = sum((self.gram / 100) * self.caloriesPer100g for _, self.gram, self.caloriesPer100g in self.foodList)
        return totalCalories

