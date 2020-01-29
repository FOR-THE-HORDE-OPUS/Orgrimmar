class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_address(self, address):
        self.address = address

    def print_info(self):
        print(f"Name: {self.name}")
