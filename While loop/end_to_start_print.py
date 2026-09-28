# print from end to start.
start = int(input("Enter a number: "))
end = int(input("Enter a number: "))

i = end
while i >= start:
    print(i, end=" ")
    i -= 1