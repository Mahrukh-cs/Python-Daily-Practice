def mutate(x):
    x[1] = 100
    x.append(99)
    print(f"Inside function = {x}")

nums = [1, 2, 3]
mutate(nums)
print(f"Outside function = {nums}")