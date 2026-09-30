for i in range(10, 0, -1):
    print(i, end=" ")

print("\n")

# this will print nothing because direction(from L to R)(positive) and sign(negative) don't match
for i in range(0, 11, -1): 
    print(i, end=" ")

print("\n")

for i in range(100, 0, -1):
    if i%2 == 0 and i%3 == 0:
        print(i, end=" ")