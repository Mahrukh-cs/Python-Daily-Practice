"""
seperate a list of integers into two distinct lists: one containing all the even numbers
and the other containing all the odd numbers. 
"""
def even_odd_list(ls):
    even_list = []
    odd_list = []
    for num in ls:
        if num %2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    print(f"Even numbers list = {even_list}")
    print(f"Odd numbers list = {odd_list}")


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd_list(nums)
