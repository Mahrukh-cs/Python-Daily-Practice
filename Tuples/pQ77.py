# take 5 numbers from user as input, store them in a tuple, and print the tuple along with its minimum and maximum.
ls = input("Enter 5 numbers: ").split()
my_tuple = tuple(ls)
print(f"Tuple = {my_tuple}")
print(f"Minimum = {min(my_tuple)}")
print(f"Maximum = {max(my_tuple)}")