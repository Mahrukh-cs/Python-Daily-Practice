# keys should be immutable. That's why we can't use list which is mutable.
dic = {
    "Computer": 99, 
    "Math": 100,
    "English": 100,
    55: 101,
    102: "Mano",
    "ls": [1,2,3],
    (4, 5): "Sun",
    # repeated key does not give error but it will give last value
    "Computer": 100
    # list can't use as key(bcz list are mutable): TypeError --> unhashable
    #[8, 9]: "True"
}
print(dic)
print(type(dic))