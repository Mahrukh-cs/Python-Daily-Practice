# make a function which return min and max of a list
def min_max(lst):
    mini = min(lst)
    maxi = max(lst)
    return maxi, mini

ls = [20, 304, 102, 4, -1, -39, 4834]
maximum, minimum = min_max(ls)
print(f"Maximum = {maximum}, type = {type(maximum)}")
print(f"Minimum = {minimum}, type = {type(minimum)}")