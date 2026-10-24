"""
Populate a dictionary with 6 student names and their corresponding scores. 
loop through it and print the names of all students who have achieved a score above 75.
"""
students = {
    "Alice": 82,
    "Bob": 67,
    "Charlie": 91,
    "Diana": 74,
    "Eve": 88,
    "Frank": 55
}
for name, mark in students.items():
    if mark > 75:
        print({name}) 