# w.r.t a function get_stats(nums) that takes a tuple of numbers 
# and returns a tuple containing the sum, average, minimum.
# Unpack the returned tuple and print each value.
def get_stats(nums):
    n = len(nums)
    total = sum(nums)
    average = total/n
    minimum = min(nums)
    tp =(total, average, minimum)
    return tp
    
tpl = (20, 30, 10, 44, 22, -1, 0)
total, average, minimum = (get_stats(tpl))
print(f"Total = {total}")
print(f"Average = {average:.2f}")
print(f"Minimum = {minimum}")
