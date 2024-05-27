class PersonView:
    def display_person(self, person):
        print(f"Name: {person.getName()}")
        print(f"Surname: {person.getSurname()}")
        print(f"Birthdate: {person.getBirthdate()}")
        print(f"Phone Number: {person.getPhoneNumber()}")
        print(f"Abbreviation: {person.getAbbreviation()}")
        print(f"Age: {person.getAge()}")
        print('\n')