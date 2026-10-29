"""
top 3 subjects by marks
given a dictionary of subjects and their marks and sort in descending order
Then, print only the top 3 subjects with their marks. 
"""
subjects = {
    "math": 99,
    "urdu": 78,
    "eng": 100,
    "sci": 88,
    "comp": 96,
    "islm": 50
}
ans = sorted(subjects.items(), key= lambda x: x[1], reverse=True)
result = ans[0:3]
for subj, mark in result:
    print(f"{subj}'s marks = {mark}")