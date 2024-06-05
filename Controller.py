from model import Model
from personView import PersonView


class Controller:

    def display_persons(self, model):
        view = PersonView()
        for person in model._persons:
            view.display_person(person)

    def display_Blutbilder(self, model):
        view = PersonView()
        for blutbild in model._Blutbilder:
            view.display_blutbild(blutbild)
