# print start to end, numbers which are divisble by 3, 4
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end):
    if i%3 == 0 and i%4 == 0:
        print(i, end=" ")