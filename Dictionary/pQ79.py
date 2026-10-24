"""
create a dictionary for student, including keys like name, age, city and marks(as a list of scores)
print each piece of information using its key.
"""
student = {
    "name": "Mano Billi",
    "age": 20,
    "city": "Lahore",
    "marks": [99, 100, 100, 100]
    }
for key, value in student.items():
    print(f"{key}: {value}")
