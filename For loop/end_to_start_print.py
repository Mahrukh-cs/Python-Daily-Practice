# print from end to start.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(end, start-1, -1):
    print(i, end=" ")