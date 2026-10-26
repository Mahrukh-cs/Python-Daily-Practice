marks = {
    "math": 85,
    "science": 92,
    "english": 78,
    "urdu": 80
}
print(f"Length of marks-dictionary = {len(marks)}")
print(f"Sum of values of marks-dictionary = {sum(marks.values())}")
print(f"Minimum = {min(marks.values())}")
print(f"Maximum = {max(marks.values())}")
# if we pass dictionary, then it will give min and max from keys not values
print(f"Minimum = {min(marks)}")
print(f"Maximum = {max(marks)}")