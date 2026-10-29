# double all marks
marks = {"math": 85, "science": 92, "english": 99, "urdu": 68}
double = {sub: mark * 2 for sub, mark in marks.items()}
print(double)