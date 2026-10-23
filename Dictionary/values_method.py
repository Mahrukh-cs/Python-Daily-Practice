marks = {
    "math": 100,
    "computer": 100,
    "English": 100,
    "science": 99,
    "physics": 99,
    "business": 100
}
total = 0
for mark in marks.values():
    total += mark

print(f"Total Marks = {total}")