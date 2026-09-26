age = int(input("Enter your age: "))
certificate = True
if age >= 18:
    if certificate == True:
        print("You will be hired")
    else:
        print("Can't hire due to no certificate")
else: 
    print("Can't hire, age is less than 18")