students = {
    101: {"name": "Mano", "age": 20, "city":"Multan",},
    102: {"name": "Mahoor", "age": 21, "city":"Lahore",},
    103: {"name": "Fatima", "age": 20, "city":"Lahore",
          "details": {"ph": 23479821658, "gender": "female"}
}
}
for roll_no, details in students.items():
    print(f"roll_no = {roll_no}, name = {details['name']}, age = {details['age']}, city = {details['city']}")