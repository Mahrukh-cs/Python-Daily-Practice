"""
wrt a function tax_calculator(income) that takes annual income and returns the tax amount based
on these slabs:
. upto 250,000 - no tax
. 250001 to 500000 - 5%
. 500001 to 1000000 - 20%
. above 1000000 - 30%
"""
def tax_calculator(income):
    if income > 1000000:
        return (30/100) * income
    elif income >= 500001 and income <= 1000000:
        return (20/100)* income
    elif income >= 250001 and income <= 500000:
        return (5/100)* income
    else:
        print("No tax")

amount = int(input("Enter your income = "))
tax_amount = tax_calculator(amount)
print(tax_amount)