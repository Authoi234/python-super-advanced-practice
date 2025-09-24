from dataclasses import dataclass, field

@dataclass(order=True)
class Car:
    sort_index: int = field(init=False, repr=False)
    name: str
    manufacturer: str
    year: int
    price: int

    def __post_init__(self):
        self.sort_index = self.price


if __name__ == "__main__":
    car1 = Car("Camry", "Toyota", 2020, 38000) 
    car2 = Car("Prado", "Toyota", 2021, 7000)
    car3 = Car("Corolla", "Toyota", 2021, 32000)
    print( car1 )
    print( car2 )
    print( car3 )
    print( car1 > car2 )
    print( car3 > car3 )