# print from start to end
start = int(input("Enter a number: "))
end = int(input("Enter a number: "))

# don't change start input value, that's why using i
i = start
print(f"Value of i is {i} before while loop.")

while i <= end:
    print(i, end=" ")
    i += 1

print(f"Value of i is {i} after while loop.")