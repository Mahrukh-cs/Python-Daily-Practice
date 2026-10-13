"""
Given 2 lists of same length. wrt python code where using a loop to create a new list 
where each element is sum of the corresponding elements from both original lists.  element-wise sum of two lists
"""
def sum_of_two_list(nums1, nums2):
    n = len(nums1)
    new_list = []
    for i in range(0, n):
        total = nums1[i] + nums2[i]
        new_list.append(total)
    return new_list

nums1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
nums2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]
print(sum_of_two_list(nums1, nums2))

