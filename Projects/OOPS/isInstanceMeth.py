# ans 9th questions:
class Car:
    def __init__(self, brand , model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand
    
    @staticmethod
    def genral_description():
        return "cars are means for transport"
    
    @property #to give only read only access
    def model(self):
        return self.__model

class EvCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


# safari= Car("TATA", "SAFARI") 
tesla = EvCar("Tesla", "F1","610kwh")

print(isinstance(tesla, Car)) #to check is this object of Car class or not
print(isinstance(tesla, EvCar)) #to check is this object of EvCar class or not

#The tesla is object of both car and EvCar we prove this using isinstance() method
