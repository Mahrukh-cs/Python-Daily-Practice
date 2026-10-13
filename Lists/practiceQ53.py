# Find the largest element. Don't use max() built-in function.
nums = [3, -1, 4, 1, 56, 0, 2, 6, 333, -222, 5050]

maxi = float("-inf")
for num in nums:
    if num > maxi:
        maxi = num

print(f"Largest number = {maxi}")