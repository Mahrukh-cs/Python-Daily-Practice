my_tuple = (100, 200, 300, "Mano", "Billi", "Sun", 99, "Moon")
n = len(my_tuple)
for i in range(0, n):
    print(my_tuple[i], end=" ")

print()

for ele in my_tuple:
    print(ele, end=" ")

print()

for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value = {value}")