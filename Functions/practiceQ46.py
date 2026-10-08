"""
wrt a function fizzbuzz(n) that takes a single number and prints "Fizz" if it's divisible by 3
, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible by both,
otherwise print number itself.
"""
def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0: 
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)

n = int(input("Enter number = "))
fizzbuzz(n)