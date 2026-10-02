"""
Take number as input from user one by one.
 Skip negative numbers and
 keep adding postive numbers.
 Stop when the user enters 0.
 Print the total. (use both continue and break)
"""

total = 0
while True:
    n = int(input("Enter number = "))
    if n == 0:
        break
    if n < 0:
        continue
    total += n

print(f"Total = {total}")