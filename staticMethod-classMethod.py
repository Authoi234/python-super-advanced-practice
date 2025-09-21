class Car():
    count:int = 0

    def __init__(self, name: str, manufacturer: str, color: str, year: int):
        print("Creating a Car")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        Car.count += 1

    def change_gear(self, gear: str) -> None:
        print("Changing gear to", gear)
    
    @staticmethod
    def latest_price(location:str, manufacturer:str, name:str) -> int | float:
        #get the price from a database or web api
        return 50000
    
    @classmethod
    def display_count(cls):
        print("Car count", cls.count)

    @classmethod
    def reset_count(cls):
        cls.count = 0

if __name__ == "__main__":
    mycar1:Car = Car("Model S", "Tesla", "Red", 2020)
    mycar2:Car = Car("Model S", "Tesla", "Red", 2020)
    mycar3:Car = Car("Model S", "Tesla", "Red", 2020)

    Car.display_count()
    Car.reset_count()
    Car.display_count()

    print(mycar1.latest_price("USA", "Tesla", "Model S"))
    print(Car.latest_price("2020", "Toyota", "Camry"))
