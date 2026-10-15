"""
create a list of containing square numbers from 1 to 10(i.e: 1, 4, 9, ...100)
"""
def square():
    ls = []
    for i in range(1, 11):
        ls.append(i*i)
    return ls

print(f"Square numbers list = {square()}")