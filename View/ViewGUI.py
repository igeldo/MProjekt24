class ViewGUI:
    def __init__(self, model):
        self._model = model

    def display_allData(self):
        blutbilder = MainModel.get_Blutbilder()
        result_text = ""
        for blutbild in blutbilder:
            result_text += f"Patienten ID: {blutbild.getPatID()}, Aufnahmedatum: {blutbild.getDate()}, Messwerte: {blutbild.getMesswerte()}\n"
        self.resultLabel.setText(result_text)