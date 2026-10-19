my_tuple = (100, 200, 300, "Mano", "Billi", "Sun", 99, "Moon")

print(my_tuple[3:])
# will reverse tuple and overwrite/reassign existing value but can't update tuple(immutable) 
# reassigning integer to tuple (allowed but updating any specific index not allowed)
# my_tuple = 6
# print(my_tuple)
my_tuple = my_tuple[::-1]
print(my_tuple)