"""
define a dictionary with five subjects and their respective marks.
Utilize the get() method to try accessing a subject that is not in dictionary, 
ensuring it prints "Not Available" as a default.
"""
marks = {
    "math": 100,
    "computer": 100,
    "English": 100,
    "physics": 99,
    "business": 100
}
# print(marks.get("computer", "Not Available"))
print(marks.get("Law", "Not Available"))