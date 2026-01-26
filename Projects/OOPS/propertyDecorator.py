# ans 8th questions:
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


safari= Car("TATA", "SAFARI") 

# safari.model="NEXON" # with out an setter method we can't update value bqz of property decorator

safari.brand = "Thar" 
print(safari.brand) # with out property decorate we can able to change value of class variable with the help of obj with using setter
print(safari.model)
