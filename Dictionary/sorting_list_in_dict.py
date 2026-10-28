marks = {
    "mano": [43, 12, 98, 10, 22],
    "billi": [76, 55, 34, 89, 61],
    "maha": [20, 45, 67, 89, 12],
    "mahu": [34, 78, 55, 89, 40],
    "maham": [78, 54, 39, 20]
}
# -1 best for last index even length of list are equal or not 
ans = sorted(marks.items(), key=lambda x: x[1][-1])
print(ans)