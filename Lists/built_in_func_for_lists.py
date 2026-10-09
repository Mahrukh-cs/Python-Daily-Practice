marks = [22, 34, 55, 2, 90, 99, 56]

# len() to find length
n = len(marks)
print(f"Length of list = {n}")

# max() to find maximum
maxi = max(marks)
print(f"Maximum marks = {maxi}")

# min() to find minimum
mini = min(marks)
print(f"Minimum marks = {mini}")

# sum() to find sum
total = sum(marks)
print(f"Total marks = {total}")

# sorted(), it will always return a new list
new_list = sorted(marks)
# for descending order --> sorted(marks, reverse=True)
print(f"New list = {new_list}")
print(f"marks list = {marks}")