# '=' means address refer 
original = [1, 2, 3]
copy = original
copy.append(100)
print(original)
print(copy)
# "is" check by refrence(address)
print(copy is original)
# "=" check by value
print(copy == original)
print(f"id of original = {id(original)}")
print(f"id of copy = {id(copy)}")


a = [4, 5, 6]
b = [4, 5, 6]
# "is" check by refrence(address)
print(b is a)
# "=" check by value
print(b == a)
print(f"id of a = {id(a)}")
print(f"id of b = {id(b)}")