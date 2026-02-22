"""
Contains Duplicate
https://neetcode.io/problems/duplicate-integer/question

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.



Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set from the list
        num_set = set(nums)

        # If len(num_set) == len(nums), no duplicates
        if len(num_set) == len(nums):
            return False
        else:
            return True
        
        # Optimal soln: return len(set(nums)) < len(nums)