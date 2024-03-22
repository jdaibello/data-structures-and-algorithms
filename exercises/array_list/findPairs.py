"""
Write a function to find all pairs in an integer array whose sum is equal to a given number.
"""

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]: # if the two numbers are the same
                continue
            elif nums[i] + nums[j] == target: # if the sum of the two numbers is equal to the target
                print(i, j)

myList = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(myList, 6)

# LeetCode solution
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num # find the complement of the current number

        if complement in seen:
            return [seen[complement], i] # return the indices of the two numbers

        seen[num] = i # store the current number and its index in the dictionary

nums = [2, 7, 11, 15]
target = 9
indices = twoSum(nums, target)
print(f'Indices of the tho numbers are: {indices}')