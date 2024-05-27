from personView import PersonView

class PersonController:
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def display_persons(self):
        view = PersonView()
        for person in self.persons:
            view.display_person(person)
