student = {
    "name": "Manan",
    "age": 22, 
    "gender": "male", 
    "city": "Paris"
    }
# print("name" in student)
# print(22 in student)
# print("city" in student)
key = input("Enter key: ")
if key in student:
    print(f"{key}'s value = {student[key]}")
else:
    print(f"{key} does not exists")