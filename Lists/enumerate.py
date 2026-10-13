nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(nums[::-1]):
    print(f"Index = {index} and value = {value}")


for index, value in enumerate(nums):
    if value %2 == 0:
        print(index)
