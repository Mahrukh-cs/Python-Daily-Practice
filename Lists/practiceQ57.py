"""
check if a list is sorted. wether it is sorted in ascending order.range
 print True if sorted else False. Don't use sorted().
"""
def is_sorted(lst):
    n = len(lst)
    for i in range(0, n-1):
        if lst[i] > lst[i+1]:
            return False
    return True

nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]
print(is_sorted(nums))
