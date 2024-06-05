from personView import PersonView


class BlutbildController:
    def __init__(self):
        self.Blutbilder = []

    def add_Blutbild(self, blutbild):
        self.Blutbilder.append(blutbild)

    def display_Blutbilder(self):
        view = PersonView()
        for blutbild in self.Blutbilder:
            view.display_blutbild(blutbild)
