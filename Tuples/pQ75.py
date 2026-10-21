# create a tuple of 8 numbers. Using slicing, print the first 3, last 3 and every alternate element.
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
first_slice = num_tuple[:3]
print(f"First three = {first_slice}")
second_slice = num_tuple[-3:]
print(f"Last three = {second_slice}")
third_slice = num_tuple[::2]
print(f"Alternate elements = {third_slice}")