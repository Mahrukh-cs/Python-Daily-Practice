"""
wrt a function power(base, exp) that returns base raised to exp using a loop - no ** operator
or pow() allowed.
"""
def power(base, exp):
    ans = 1
    for i in range(exp):
        ans = ans * base
    return ans


print(power(2, 3))
print(power(3,3))
print(power(5,5))
print(power(11,0))