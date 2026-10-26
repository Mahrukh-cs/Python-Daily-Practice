students = {
    101: {"name": "Mano", "age": 20, "city":"Multan",},
    102: {"name": "Mahoor", "age": 21, "city":"Lahore",},
    103: {"name": "Fatima", "age": 20, "city":"Lahore",
          "details": {"ph": 23479821658, "gender": "female"}
}
}
# how to access
print(students[101])
print(students[102]["age"])
print(students[103]["details"]["gender"])