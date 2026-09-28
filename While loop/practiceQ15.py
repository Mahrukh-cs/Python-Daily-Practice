# print all numbers which are divisible by 3 and 5, from 1 to 100
start = 1
end = 100
i = start
while start >= end:
    if i%3 == 0 and i%5 == 0:
        print(i, end=" ")
    i += 1