name = "Mano Billi"
age = 20
gender = "Female"

# using comma seperator
print("Student name is",name, "and her age is",age, "and gender is", gender)
# using '+' operator
# typeerror: can't concatenate str with int, only string with string
# print("Student name is " + name + " and her age is " + age + " and gender is " + gender)
print("Student name is " + name + " and her gender is " + gender)


# using sep and end
# sep: string inserted between values, by default a space
print(name, age, gender, sep="@@")
# end: string appended after last value, by default newline
print(name, end=" ")
print(age, end=" ")
print(gender)


# using f strings
print(f"Student name is {name}, age is {age} and her gender is {gender}.")