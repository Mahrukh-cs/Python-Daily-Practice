"""
wrt a lambda function that takes a number and returns "Positive", or "Negative".
"""
# def abc(n):
#     if n >= 0:
#         return "Positive"
#     return "Negative"

is_positive = lambda n: "Positive" if n >= 0 else "Negative"

print(is_positive(2))
print(is_positive(-1))