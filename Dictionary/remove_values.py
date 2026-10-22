student = {
    "name": "Manan",
    "age": 22, 
    "gender": "male", 
    "city": "Paris"
    }
print(student, id(student))
# # .pop() --> requires key : delete from dictionary
# student.pop("name")
# print(student, id(student))
# # clear() --> deletes/clears the whole dictionary
# student.clear()
# print(student, id(student))
# del student
# print(student, id(student))
# nameError: student name is not defined 

del student["age"]
print(student, id(student))