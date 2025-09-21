from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, name: str, manufacturer: str, color: str):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction: str) -> None:
        print("Turning",self.name, "to",direction)

    @abstractmethod
    def change_gear(self, gear: str) -> None:
        pass

class Car(Vehicle):
    def __init__(self, name: str, manufacturer: str, color: str, year: int):
        super().__init__(name, manufacturer, color)
        self.year = year

    def change_gear(self, gear: str) -> None:
        print("Changing gear to", gear)

if __name__ == "__main__":
    mycar:Car = Car("Model S", "Tesla", "Red", 2020)
    print(mycar.name)
    mycar.turn("left")
    mycar.change_gear("D")