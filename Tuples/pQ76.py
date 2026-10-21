# create a tuple of marks of 6 students. print highest, lowest, average and total.
marks_tple = (33, 50, 99, 100, 0, 94)
n = len(marks_tple)
highest = max(marks_tple)
lowest = min(marks_tple)
total = sum(marks_tple)
average = total/n
print(f"Highest marks = {highest}")
print(f"Lowest marks = {lowest}")
print(f"Total marks = {total}")
print(f"Average marks = {average:.2f}")