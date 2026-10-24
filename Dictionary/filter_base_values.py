marks = {
    "math": 100,
    "computer": 100,
    "English": 100,
    "science": 99,
    "physics": 99,
    "business": 100
}
print(f"\n---Subject Performance---")
for subject, score in marks.items():
    if score >= 80:
        print(f"{subject} = Excellent")
    elif score >= 60:
        print(f"{subject} = Good")
    else:
        print(f"Needs Improvement")


# counting values that match a condition (using .value() directly here)
passed_subjects = 0
for score in marks.values():
    if score >= 60:
        passed_subjects += 1
print(f"\n Subject Passed = {passed_subjects}")