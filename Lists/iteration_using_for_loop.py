nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n = len(nums)
# sum = 0
# for i in range(0, n):
#     sum += nums[i]
# print(f"Sum of list = {sum}")


# alternate method 
total = 0
for num in nums:
    total += num

print(f"Sum of list = {total}")


# print reverse
print("Reverse Printing = ", end=" ")
for num in nums[::-1]:
    print(num, end=" ")