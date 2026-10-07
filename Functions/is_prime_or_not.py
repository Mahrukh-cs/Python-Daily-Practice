# return True if a number is prime else return false
def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        return True
    return False

print(is_prime(9))
print(is_prime(17))
print(is_prime(8))
