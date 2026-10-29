# create a dict from two lists
subjects = ["math", "science", "english"]
scores = [85, 97, 99]
result = {s: sc for s, sc in zip(subjects, scores)}
print(result)