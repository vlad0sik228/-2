import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car='None'):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car
        self.mess = 80

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.setiety > 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness += self.job.gladness_less
        self.satiety -= 4


    def shopping(self):
     pass

    def chill(self):
        if self.gladness < 50:

           self.mess -=20
    def clear_home(self):
        if self.mess():
           self.mess += 0:
        else:
           self.gladness = 0

    def to_repair(self):
        if self.strenght():
           self.strenght += 100:
        else:
           self.money():
           self.money -= 100

def indexes_day(self, day):
    pass


def is_alive(self):
    pass


def live(self):
    pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumpton']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot mave...')
            return False


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, "gladness_less": 10},
            'C++': {'salary': 80, "gladness_less": 5},
            'Python': {'salary': 30, "gladness_less": 8},
            'Rust': {'salary': 60, "gladness_less": 11}}

brand_of_car = {'BMW': {'fuel': 100, 'strenght': 100, 'consumption': 15},
                'Lada': {'fuel': 70, 'strenght': 20, 'consumption': 8},
                'Volvo': {'fuel': 90, 'strenght': 85, 'consumption': 10},
                'Ford': {'fuel': 60, 'strenght': 90, 'consumption': 17}}
print(brand_of_car.keys())
print(list(brand_of_car))
