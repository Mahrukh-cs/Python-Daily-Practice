"""
given a list of marks, use list comprehension to create a new list
that contains only the marks that are above 75.
"""
marks = [40, 60, 88, 90, 99, 78, 97, 99, 100, 11]
# filter
marks_list = [num for num in marks if num > 75]
print(marks_list)