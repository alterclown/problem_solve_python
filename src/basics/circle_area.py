import math

def circle_area(radius):
    if radius >= 0:
        area = math.pi * radius ** 2
        print("area of circle",area)
    else:
        print("area of circle is zero")

result = circle_area(-3)
