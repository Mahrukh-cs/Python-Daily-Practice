# take 2 no as input. without using *, calculate and print their product using += in a way
# that adds the first number to itself and second number of times

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
product = 0
for i in range(1, num2+1):
    product += num1
print(f"Product of {num1} and {num2} = {product}")