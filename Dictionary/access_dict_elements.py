dic = {
    "Computer": 99, 
    "Math": 100,
    "English": 100,
    1: 101,
    102: "Mano",
    "ls": [1,2,3],
    (4, 5): "Sun",
    # list can't use as key(bcz list are mutable): TypeError --> unhashable
    #[8, 9]: "True"
}
print(dic[1])
print(dic["Computer"])
print(dic["Math"])
print(dic["English"])
print(dic["ls"])
# KeyError: key not present
# print(dic["abc"])


# key method
# .get() --> return value
print(dic.get("Computer", -1))

# Q: print marks if key exist otherwise print Subject not found
# by me
subject = "Computer"
if subject in dic:
    print(f"Marks scored in {subject} = {dic[subject]}")
else:
    print("Subject Not Found")

# other method
subject = "English"
ans = dic.get(subject)
# if ans == None            
if ans is None:
    print("Subject Not Found")
else:
    print(f"Marks scored in {subject} = {ans}")