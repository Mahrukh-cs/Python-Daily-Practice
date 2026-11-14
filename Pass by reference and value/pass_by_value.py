# immutable objects are pass by value
def add_number(x):
    x = x + 1
    print(f"Inside function = {x}")

num = 8
add_number(num)
print(f"Outside function = {num}")