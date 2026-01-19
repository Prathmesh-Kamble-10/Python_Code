import math

def circleMath(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circum=circleMath(5)

print("Area of circle is = ", area)
print("Circumference of circle is = ", circum)

