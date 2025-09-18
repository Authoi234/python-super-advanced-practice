class Car:
    def __init__(self, name, manufacture, year):
        self.name = name
        self.manufacture = manufacture
        self.year = year

    def __repr__(self):
        return "Car('{}', '{}', {})".format(self.name, self.manufacture, self.year)
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.manufacture, self.year)

if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2020)
    print(my_car)
    print(repr(my_car))