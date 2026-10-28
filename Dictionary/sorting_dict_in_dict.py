students = {
    "mano": {"math":43, "english":12, "computer":98},
    "billi": {"math":76, "english":55, "computer":34},
    "maha": {"math":20, "english":45, "computer":67},
    "mahu": {"math":34, "english":78, "computer":55},
    "maham": {"math":78, "english":54, "computer":44 }
}
# for descending order
# ans = dict(sorted(students.items(), key= lambda x: x[1]["math"]))
# print(ans)
# ans = dict(sorted(students.items(), key= lambda x: x[1]["math"], reverse=True))


# on the basis of sum of dictionay
# ans1 = dict(sorted(students.items(), key= lambda x: x[1]["math"] + x[1]["english"] + x[1]["computer"]))
ans1 = dict(sorted(students.items(), key= lambda x: sum(x[1].values())))
print(ans1)
# for descending order
# ans1 = dict(sorted(students.items(), key= lambda x: sum(x[1].values()),reverse=True))
