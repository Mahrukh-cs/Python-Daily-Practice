"""
student details
create a nested dictionary details for 4 students, 
where each students entry includes
their name, age and city. 
write a loop to print full detail of each student in a clear readable format.
"""
details = {
    101: {"name": "Mano", "age": 20, "city": "Multan"},
    102: {"name": "Bano", "age": 22, "city": "Lahore"},
    103: {"name": "Dano", "age": 21, "city": "Islamabad"},
    104: {"name": "Tano", "age": 23, "city": "Gujaranwala"}
}
for rollno, detail in details.items():
    print(f"roll_no = {rollno}, name = {detail['name']}, age = {detail['age']}, city = {detail['city']}")
