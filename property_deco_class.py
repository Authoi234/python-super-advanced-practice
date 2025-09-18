class Car:
    def __init__(self, name, manufacture, year, price:None):
        self.name = name
        self.manufacture = manufacture
        self.year = year
        self._price = price

    @property
    def price(self):
        return '${:.2f}'.format(self._price)
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            print("Invalid data for price")
        elif new_price < 0:
            print("Price cannot be negative")
        else:
            self._price = new_price

    @price.deleter
    def price(self):
        self._price = None

if __name__ == "__main__":
    car = Car("Carmy", "Toyota", 2022, 10000)
    print(car.price)
    car.price = 43330
    print(car.price)
    car.price = "100"
    print(car.price)
