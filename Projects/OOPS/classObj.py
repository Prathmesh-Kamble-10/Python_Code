# first question ans.

# def car(model,brand):
#     print(f"{model} and {brand}")


# car("classic10","BMW")


class Car:
    brand = None
    model = None
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    
    def carInfo(self):
        return(f"its very good car")


print("-------------------------")
my_car = Car("Toyota","Xen")
print("Brand : ",my_car.brand)
print("Model : ",my_car.model)
print("Description : ",my_car.carInfo())

print("-------------------------")
my_new_car = Car("BMW","X1")
print("Brand : ",my_new_car.brand)
print("Model : ",my_new_car.model)
print("Description : ",my_new_car.carInfo())
print("-------------------------")


# class Car:
#     brand = None
#     model = None
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# print("car 1: ")
# audi = Car("Audi","classic10")
# print("Brand : ",audi.brand)
# print("Model : ",audi.model)

# print("\n\n")
# print("car 2: ")
# Honda = Car("Honda","Honda City")
# print("Brand : ",Honda.brand)
# print("Model : ",Honda.model)


# print("\n\n")
# print("car 2: ")
# bmw = Car("BMW","X1")
# print("Brand : ",bmw.brand)
# print("Model : ",bmw.model)
