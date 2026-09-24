"""
Must start with a letter or underscore(_)
can contain letters, digits and underscores
cannot start with a digit
cannot use python keywords(if, for, while...)
names are case-sensitive --> age != Age != AGE
"""
# valid but not making sense
_ = 10

# valid
age1 = 11
age = 23
Age_1 = 21

# not valid
# 1age = 12

print(_, age, age1, Age_1)
