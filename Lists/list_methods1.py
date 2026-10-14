"""
append() -> add at end/last 
insert() -> add at specific index
remove(value) -> remove by value(pass value only) not by index
pop(index) -> remove last occurence by default otherwise remove value at given index
"""
ls = ["Mano", 20, "Female", 3.3]
ls.append("CS")
ls.append("Billi")
print(ls)
ls.insert(3, "Software Engineer")
print(ls)
x = ls.pop()
print(x)
print(ls)
ls.remove(3.3)
print(ls)