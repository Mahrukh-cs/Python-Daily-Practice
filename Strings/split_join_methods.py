"""
string methods: split() and join()
split(): Break string to list
join(): Combine List into string
"""
text = "Mah Rukh is Software Engineer"
# print(len(text.split(" ")))

# only string will join, no numbers 
my_list = ["M","a","h","r","u","k","h"]
my_list1 = ["M","a","h","r","u","k","h", 9, 99.99]
ans1 = "".join(str(ch) for ch in my_list1)
print(ans1)
# wrong way to string
# print(str(my_list))
ans = "".join(my_list)
print(ans)