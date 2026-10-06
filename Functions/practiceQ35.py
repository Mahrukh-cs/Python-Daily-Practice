"""
write a function that ask a number from user and prints if that number is odd or even.
"""
def odd_even():
    n = int(input("Enter number = "))
    if n%2 != 0:
        return print(f"{n} is odd.")
    else:
        return print(f"{n} is even.")

odd_even()
odd_even()