# a student scored in 3 subjects. take all three as input, calculate the total, average and print both using an f-strings.
physics = int(input("Enter your physics's marks: "))
math = int(input("Enter your math's marks: "))
english = int(input("Enter your english's marks: "))

total = physics + math + english
average = total/3
print(f"Your toatl marks is {total} and average marks is {average:.2f}")
