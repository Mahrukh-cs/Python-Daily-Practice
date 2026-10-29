# to print keys and squares as values
square = {}
# for i in range(1, 11):
#     square[i] = i * i
# print(square)

square = {i: i * i for i in range(1, 11)}
print(square)