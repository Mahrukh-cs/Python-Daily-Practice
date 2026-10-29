"""
filter passing marks
given an existing dictionary of subjects and their respective marks,
use dictionary comprehension to generate a new dictionary that contains only the subjects
where the student scored 40 or more(i.e: passed)
"""
data = {
    "math": 99,
    "urdu": 33,
    "eng": 100,
    "sci": 39,
    "comp": 96,
    "islm": 50
}
result = {s: m for s, m in data.items() if m >= 40}
print(result)