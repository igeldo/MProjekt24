class Person:
    def __init__(self, name, age, sex, fitness_level):
        self.name = name
        self.age = age
        self.sex = sex
        self.fitness_level = fitness_level

    def get_properties(self):
        return {
            'Name': self.name,
            'Age': self.age,
            'Sex': self.sex,
            'Fitness Level': self.fitness_level
        }

    def get_resting_heart_rate(self):
        if self.sex == 'male':
            if self.age < 30:
                if self.fitness_level == 'excellent':
                    return 65
                elif self.fitness_level == 'good':
                    return 68
                elif self.fitness_level == 'low':
                    return 72
            elif 30 <= self.age < 50:
                if self.fitness_level == 'excellent':
                    return 67
                elif self.fitness_level == 'good':
                    return 70
                elif self.fitness_level == 'low':
                    return 74
            elif self.age >= 50:
                if self.fitness_level == 'excellent':
                    return 70
                elif self.fitness_level == 'good':
                    return 72
                elif self.fitness_level == 'low':
                    return 76
        elif self.sex == 'female':
            if self.age < 30:
                if self.fitness_level == 'excellent':
                    return 68
                elif self.fitness_level == 'good':
                    return 71
                elif self.fitness_level == 'low':
                    return 75
            elif 30 <= self.age < 50:
                if self.fitness_level == 'excellent':
                    return 70
                elif self.fitness_level == 'good':
                    return 73
                elif self.fitness_level == 'low':
                    return 77
            elif self.age >= 50:
                if self.fitness_level == 'excellent':
                    return 73
                elif self.fitness_level == 'good':
                    return 76
                elif self.fitness_level == 'low':
                    return 80

    def get_maximum_heart_rate(self):
        return 220 - self.age
