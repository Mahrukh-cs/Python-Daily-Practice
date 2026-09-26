"""
A shop gives discount based on purchase amount:
Above 5000 --> 20%
Above 2000 --> 10%
Above 1000 --> 5%
1000 or below --> no discount
"""
purchased_amount = int(input("Enter your purchased amount: "))
if purchased_amount >= 5000:
    print("Discount: 20%")
elif purchased_amount >= 2000 and purchased_amount < 5000:
    print("Discount: 10%")
elif purchased_amount >= 1000 and purchased_amount < 2000:
    print("Discount: 5%")
elif purchased_amount >= 0 and purchased_amount < 1000:
    print("No Discount")  
else:
    print("Please, enter a valid amount") 