import copy
original = [54, 2, 3, [5, 6, 7], 8, 9]
# shallow_copy = original.copy()
shallow_copy = copy.deepcopy(original)

print(original)
print(shallow_copy)

print(id(original))
print(id(shallow_copy))

shallow_copy[4] = 999
print(original)
print(shallow_copy)

shallow_copy[3][1] = 1000
print(original)
print(shallow_copy)