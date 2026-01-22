# ans 4th questions:

class Car:
    __brand = None #private variable
    __model = None #private variable

    def get_brand(self): #getter
        return self.__brand
    
    def set_brand(self,brand): #setter
        self.__brand = brand

    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
my_car = Car()
my_car.set_brand("Honda")
my_car.set_model("City")
print(my_car.full_name())
print("Car Description : ",my_car.get_brand()," : ", my_car.get_model())

