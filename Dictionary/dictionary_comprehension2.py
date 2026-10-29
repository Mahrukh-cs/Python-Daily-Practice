# keep subjects where marks > 80
marks = {"math": 85, "science": 92, "english": 99, "urdu": 68}
top = {sub:mark for sub, mark in marks.items() if mark > 80}
print(top)