class Person:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def add_car(self, car):
        self.cars.append(car)

    def print_info(self):
        print(f"Name: {self.name}\n\n")
        print(f"Address: {self.address}\n\n")
