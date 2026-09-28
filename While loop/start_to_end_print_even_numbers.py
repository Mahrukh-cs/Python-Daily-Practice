# print even numbers from start to end
start = int(input("Enter number: "))
end = int(input("Enter number: "))

i = start
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1