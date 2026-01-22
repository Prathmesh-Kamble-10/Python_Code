# answer of 3rd question:
class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class EvCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
ev_tesla = EvCar('tesla','tesla-xuv','500kwh')
print(ev_tesla.full_name())
print(ev_tesla.battery_size)