"""
student marks analysis
design a dictionary where each student's name and the corresponding value
is a list of their marks with 3 different subjects. 
calculate and print the total marks and average marks for each student.
"""
students = {
    "mano": [44, 66, 88],
    "bano": [55, 77, 90],
    "tano": [87, 98, 65],
    "dano": [39, 90, 78]
}
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name}'s total marks is {total} and average marks = {avg:.2f}")