marks = {
    "math": 99,
    "science": 88,
    "computer": 100,
    "english": 89
}

print("Sorting via keys")
print(dict(sorted(marks.items(), key=lambda x: x[0])))


ans = dict(sorted(marks.items(), key=lambda x: x[1]))
print("Sorting via values")
print(ans)