fruits = ["Apple", "Banana", "Orange"]
# copy() --> returns a shallow copy of list
new_fruits_list = fruits.copy()
print(f"Fruit list before appending Grapes = {fruits}")
fruits.append("Grapes")
print(f"Fruit list after appending = {fruits}")
print(f"Copy Fruit list = {new_fruits_list}")

