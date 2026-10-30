# remove(), discard(), pop(), clear()
fruits = {"apple", "banana", "kiwi", "orange"}
# fruits.remove("kiwi")
# raise keyError if not exists
# fruits.remove("appllee")
# discard() --> does'nt raise keyerror
# fruits.discard("orange")
# fruits.discard("applle")
# pop() --> it randomly removes item from set and we can stored in a variable
# removed = fruits.pop()
# print(removed)
# clear() --> clears whole set 
fruits.clear()
print(fruits)
