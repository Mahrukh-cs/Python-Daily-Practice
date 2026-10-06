"""
write a function called "rectangle_area" that takes length and breadth as parameters 
and print the area.
"""
def rectangle_area(l, b):
    rectangle_area = l * b
    print(f"Area of rectangle = {rectangle_area}")

length = int(input("Enter length = "))
breadth = int(input("Enter breadth = "))
rectangle_area(length, breadth)