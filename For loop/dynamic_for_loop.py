start = int(input("Enter your start number: "))
end = int(input("Enter your end number: "))
total = 0

for i in range(start, end+1):
    total += i

print(f"Total = {total}")
