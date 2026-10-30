# real world example: students records
math_students = {"mano", "billi", "john"}
science_students = {"john", "mano", "berkely"}
print("Students in both math and science")
# print(math_students & science_students)
print(math_students.intersection(science_students))

print("Students in either math or science")
# print(math_students | science_students)
print(math_students.union(science_students))
