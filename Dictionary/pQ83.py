"""
given a dictionary of marks for different subjects, loop over its values() to calculate 
and print the total and average marks obtained. 
"""
marks = {
    "math": 100,
    "computer": 100,
    "English": 100,
    "science": 99,
    "physics": 99,
    "business": 100
}
total = 0
n = len(marks)
# total = sum(marks.values())
# other way
for value in marks.values():
    total += value

print(f"Total marks = {total}")
average = total/n
print(f"Average marks = {average:.2f}")