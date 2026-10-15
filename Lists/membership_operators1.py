nums = [1, 2, 3, 4, 5, 7, 8, 9, 1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5, 10, 9]

target = int(input("Enter target number = "))
if target in nums:
    nums.remove(target)
    print(nums)
else:
    print("Cannot remove target, target does not exists")

