# Explicit Conversion
num1 = "100"
num2 = "200"

print(num1+num2)
print(int(num1)+int(num2))

# ValueError: Invalid literal(we need a integer to convert in integer)
num3 = ("100.5")
num4 = "100abc" # also invalid abc can't be convert
# print(int(num1)+int(num3))

a = 900.9
print(int(a))
