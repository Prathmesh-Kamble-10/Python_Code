# ans 7th questions:
class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def genral_description():
        return "cars are means for transport"

class EvCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

# evTesla = EvCar('Tesla','Tesla-xuv','500kwh')
# print(evTesla.fuel_type())        


safari= Car("TATA", "SAFARI") 
print(safari.fuel_type()) 
print(Car.genral_description())  


# print(ev_tesla.full_name())
# print(ev_tesla.battery_size)
