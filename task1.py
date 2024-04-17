class Vahacle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        print(f"Марка : {self.make}")
        print(f"Модель : {self.model}")


class Car(Vahacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels
    
    def get_info(self):
        super().get_info()
        print(f"Кількість колес: {self.wheels}")


class Moto(Vahacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels
    
    def get_info(self):
        super().get_info()
        print(f"Кількість колес: {self.wheels}")


base_class = Vahacle('Авто', 'Мотоцикл')
base_class.get_info()
print(100 * '_')
car_class = Car('Honda', 'Accord', 4)
car_class.get_info()
print(100 * '_')
moto_class = Moto('Honda', 'Dio', 2)
moto_class.get_info()
