"""
subjects and marks
create a dictionary of 6 subjects and their respective marks. 
print the subject with highest marks and the one with lowest marks, 
using max() and min() functions alongside a lambda expression.
"""
data = {
    "math": 99,
    "urdu": 78,
    "eng": 100,
    "sci": 88,
    "comp": 96,
    "islm": 50
}
maximum = max(data.items(), key= lambda x: x[1])
minimum = min(data.items(), key= lambda x: x[1])
print(f"Maximum = {maximum}")
print(f"Minimum = {minimum}")