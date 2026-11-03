text = "Python"
n = len(text)

# for i in range(0,n):
#     print(text[i])

# for char in text:
#     print(char)

# count how many times o is present?
# total = 0
# for char in text:
#     if char == "o" or char == "O":
#         total += 1
# print(total)


# while loop
# i = 0
# while i < n:
#     print(text[i])
#     i += 1


# by default indexstart value is 0
for index, char in enumerate(text, start=2):
    print(f"index = {index} and char = {char}")
