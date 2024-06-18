class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        print(f"Марка : {self.make}")
        print(f"Модель : {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels
    
    def get_info(self):
        super().get_info()
        print(f"Кількість колес: {self.wheels}")


class Moto(Vehicle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels
    
    def get_info(self):
        super().get_info()
        print(f"Кількість колес: {self.wheels}")


class Electric:
    def __init__(self):
        self.__battery = 0

    def charge(self):
        self.__battery = 100
        print("Заряд батареї: 100%")

    def get_battery(self):
        return self.__battery


class ElectricCar(Car, Electric):
    def __init__(self, make, model, wheels):
        Car.__init__(self, make, model, wheels)
        Electric.__init__(self)


class ElectricMoto(Moto, Electric):
    def __init__(self, make, model, wheels):
        Moto.__init__(self, make, model, wheels)
        Electric.__init__(self)


base_class = Vehicle('Авто', 'Мотоцикл')
base_class.get_info()
print(100 * '_')

car_class = Car('Honda', 'Accord', 4)
car_class.get_info()
print(100 * '_')

moto_class = Moto('Honda', 'Dio', 2)
moto_class.get_info()
print(100 * '_')

electric_car = ElectricCar('Tesla', 'Model S', 4)
electric_car.get_info()
electric_car.charge()
print(f"Батарея: {electric_car.get_battery()}")
print("MRO для ElectricCar:", ElectricCar.mro())
print(100 * '_')

electric_moto = ElectricMoto('Zero', 'FX', 2)
electric_moto.get_info()
electric_moto.charge()
print(f"Батарея: {electric_moto.get_battery()}")
print("MRO для ElectricMoto:", ElectricMoto.mro())