class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f'Names of {self.brand} passengers')
            for passenger in self.passengers:
                print(passenger.name)

kate = Human('Kate')
nick = Human('Nick')
car = Auto('BMW')
car.add_passengers(kate)
car.add_passengers(nick)
car.print_passengers_name()

