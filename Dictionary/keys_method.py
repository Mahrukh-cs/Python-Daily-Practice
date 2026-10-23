marks = {
    "math": 100,
    "computer": 100,
    "English": 100,
    "science": 99,
    "physics": 99,
    "business": 100
}
total = 0
for subj in marks.keys():
    print(f"Subject = {subj} and Marks = {marks[subj]}")
    total += marks[subj]

print(f"Total Marks = {total}")