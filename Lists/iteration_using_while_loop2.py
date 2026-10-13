nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n = len(nums)
# i = n-1
# while i >= 0:
#     print(nums[i], end=" ")
#     i -= 1


# count even numbers
count = 0
i = n-1
while i>= 0:
    if nums[i] %2 == 0:
        count += 1
        i -= 1

print(f"Count = {count}")