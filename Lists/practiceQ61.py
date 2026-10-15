"""
given a list, remove all duplicate elements while preserving the original order of the unique 
items.
"""
def remove_duplicate(ls):
    n = len(ls)
    result = []
    for i in range(0, n):
        if ls[i] not in result:
            result.append(ls[i])
    return result

data = [1, 7, 7, 6, 5, 5, 1, 1, 7, 8, 9, 10, 10]
print(remove_duplicate(data))