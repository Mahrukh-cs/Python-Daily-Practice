"""
combine lists into dictionary 
you have two seperate lists: one containing subject names and another containing corresponding 
create a dictionary list using dictionary comprehension, mapping each subject to its mark.
"""
subjects = ["math", "comp", "eng"]
marks = [100, 99, 98]
new_dict = {s: m for s, m in zip(subjects, marks)}
print(new_dict)