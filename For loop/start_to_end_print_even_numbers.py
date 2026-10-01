# print even numbers from start to end
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end):
    if i%2 == 0:
        print(i, end=" ")