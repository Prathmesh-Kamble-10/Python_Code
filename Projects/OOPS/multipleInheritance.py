# ans 10th questions:
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

class Engine:
    def engine_info(self):
        return "Super power engine"

class Battery:
    def battery_info(self):
        return "Fully rechargable battery"

class NewEV(EvCar,Engine,Battery,Car): # multiple inheritances
    pass

wagnor = NewEV("Suzuki", "Wagon-R Classic","100kwh")
print("Brand : ",wagnor.get_brand())
print("Model : ",wagnor.model)
print("Engine_Info : ",wagnor.engine_info())
print("Battery_Info : ",wagnor.battery_info())
print("Battery_Size",wagnor.battery_size)