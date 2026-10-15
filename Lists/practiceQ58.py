"""
Find the largest and smallest number in a list without using built-in functions like
max() and min().
hint: use a loop and a variable to track 
"""
def find_smallest(ls):
    smallest = float("+inf")
    n = len(ls)
    for i in range(0, n):
        if ls[i] < smallest:
            smallest = ls[i]
    return smallest

def find_largest(ls):
    largest = float("-inf")
    n = len(ls)
    for i in range(0, n):
        if ls[i] > largest:
            largest = ls[i]
    return largest

nums = [10, 3, 2, 5, 9, -1, 60, 90, 99, -11]
smallest = find_smallest(nums)
largest = find_largest(nums)

print(f"Smallest = {smallest}")
print(f"Largest = {largest}")
