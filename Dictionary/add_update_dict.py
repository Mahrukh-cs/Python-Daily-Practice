student = {
    "name": "Mano",
    "age": 19
}
print(student["age"], id(student))
# update
student["age"] = 20
print(student["age"], id(student))
# Add
student["gender"] = "female"

student.update(
    {"city": "Paris",
     "phone": 9321321321,
     "state": "London"
     }
)
print(student, id(student))
