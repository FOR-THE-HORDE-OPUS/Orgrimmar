class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_address(self, address):
        self.address = address

    def find_school_in_area(self):
        school_finder.find_school_by_address(self.address)

    def print_info(self):
        print(f"Name: {self.name}")
