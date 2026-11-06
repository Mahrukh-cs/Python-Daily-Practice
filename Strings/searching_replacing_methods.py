"""
String Methods: Searching and replacing
count(): substring frequency
find(): locate first occurence
index(): locate(with error)
replace(): substitute strings
"""
text = "Mah Rukh Urooj is computer science student"
print(text.count("M"))
print(text.find("Mah"))
print(text.find("Rukh"))
# find does'nt give error, give -1
print(text.find("z"))
print(text.index("Mah"))
# index give you valueError: substring not found
# print(text.index("z"))
print(text.replace("a", "z"))