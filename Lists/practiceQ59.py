"""
Reverse a list without using the .reverse() method or list slicing ([::-1])
hint : think of swaping
"""
# my method
# def reverse_list(ls):
#     n = len(ls)
#     first = 0
#     last = n-1
#     while first <= last:
#         ls[first], ls[last] = ls[last], ls[first]
#         first +=1
#         last -=1
#     return ls


# other method
def reverse_list(ls):
    n = len(ls)
    new_list = []
    for i in range(n-1, -1, -1):
        new_list.append(ls[i])
    return new_list


nums = [10, 3, 2, 5, 9, -1, 60, 90, 99, -11]
print(f"Before reversing = {nums}")
ans = reverse_list(nums)
print(f"Before reversing = {ans}")
