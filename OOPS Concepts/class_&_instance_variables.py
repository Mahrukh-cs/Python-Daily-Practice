class Student:
    school = "Allama Iqbal"

    def __init__(self, name:str):
        self.name = name

s1 = Student("Mano")        
s2 = Student("Billi")   
print(s1.name)  # Instance variable
print(s2.name)  # Instance variable

print(s1.school)        # Class variable
print(s2.school)        # Class variable
print(Student.school)   # Class variable

# way to change class variable 
Student.school = "M.A Jinnah"

print(s1.school)    # Class variable
print(s2.school)    # Class variable
print(Student.school)   # Class variable


# this does not change class variable, it will only change s1 object variable
# s1.school = "Mano Billi"
# print(s1.school)    # Class variable
# print(s2.school)    # Class variable
# print(Student.school)   # Class variable