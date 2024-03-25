"""
Return true if the list contains duplicate elements, false otherwise.
"""

def containsDuplicate(nums):
    return len(nums) != len(set(nums))