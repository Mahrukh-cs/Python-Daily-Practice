"""
given a list of numbers, use a loop to calculate and print their average.
calculate the average. use len() but don't use sum() for total.
"""
def calculate_average(nums):
    n = len(nums)
    sum = 0
    for num in nums:
        sum += num

    return sum/n


scores = [85, 90, 78, 92, 88]
average = calculate_average(scores)
print(f"Average score = {average:.2f}")

