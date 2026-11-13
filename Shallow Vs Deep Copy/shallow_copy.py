import copy
original = [1, 2, 3]
# shallow_copy = original.copy()
shallow_copy = copy.copy(original)

print(original)
print(shallow_copy)

print(id(original))
print(id(shallow_copy))

shallow_copy.append(100)

print(original)
print(shallow_copy)