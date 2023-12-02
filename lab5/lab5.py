class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname}, '


class Driver(Person):
    def __init__(self, name, surname, experience) -> None:
        super().__init__(name, surname)
        self.experience = experience

    def __str__(self) -> str:
        return super().__str__() + f'Стаж вождения: {self.experience}'


class Engine:
    def __init__(self, power, company) -> None:
        self.power = power
        self.company = company

    def __str__(self) -> str:
        return f'{self.power} л.с., {self.company}'


class Car:
    def __init__(self, brand, car_class, weight, driver: Driver, engine: Engine) -> None:
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def __str__(self) -> str:
        return f'Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} кг, Водитель: {self.driver}, Мотор: {self.engine}'

    def start(self):
        print('Поехали!')

    def stop(self):
        print("Останавливаемся")

    def turnRight(self):
        print("Поворот направо")

    def turnLeft(self):
        print("Поворот налево")


class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver: Driver, engine: Engine, carrying) -> None:
        super().__init__(brand, car_class, weight, driver, engine)
        self.carrying = carrying

    def __str__(self) -> str:
        return super().__str__() + f'\nГрузоподъемность: {self.carrying//1000} т.'


class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver: Driver, engine: Engine, horsepower) -> None:
        super().__init__(brand, car_class, weight, driver, engine)
        self.horsepower = horsepower

    def __str__(self) -> str:
        return super().__str__() + f'\nПредельная скорость: {self.horsepower} км/ч'


driver1 = Driver(name='Доминик', surname='Торетто', experience=10)
engine1 = Engine(power=375, company='Dodge')
car1 = SportCar(brand='Dodge Charger R/T SE', car_class='Muscle Car',
                weight=1760, horsepower=211, engine=engine1, driver=driver1)

driver2 = Driver('Райбек', 'Ким', 21)
engine2 = Engine(250, "Subaru")
car2 = Car("Subaru Impreza", "Седан", 1270, driver2, engine2)

driver3 = Driver('Милена', 'Жолтаева', experience=10)
engine3 = Engine(800, 'Volvo')
car3 = Lorry('Volvo FH Classic Globetrotter XL',
             'Грузовик', 7920, driver3, engine3, 325000)

for car in (car1, car2, car3):
    print(car)
    print()
