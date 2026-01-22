# second question ans.
class Car:
    brand = None
    model = None
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

print("--------------------------------")
my_car = Car("Toyota","Xen")
print("Car Description : ",my_car.full_name())

print("--------------------------------")
my_new_car = Car("BMW","X1")
print("Car Description : ",my_new_car.full_name())
print("--------------------------------")
