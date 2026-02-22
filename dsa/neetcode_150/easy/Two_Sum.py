"""
Two Sum
https://neetcode.io/problems/two-integer-sum/question

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Brute force approach
        Comparing the addition of all possible combinations

        for i in range(len(nums)):
            for j in range(len(nums)):
                # Should not reconsider the initial number
                if i == j:
                    continue
                elif nums [i] + nums[j] == target:
                    return [i, j]
                else:
                    continue
        """

        # Optimal: Using a hashmap to store the unmatching 'seen' numbers till we find the required number
        seen = {}

        # Using enumerate to get the index of the values
        for index, value in enumerate(nums):
            # Find the required number which is target - current number
            required_num = target - value

            # If the required number is not in seen dict, add the current number there with its index
            # This is because the current number can be the required number for a later number
            if required_num not in seen:
                seen[value] = index
            
            # If the required number is already in the seen dict, we found the pair.
            # Return the index of the required number first because we need sorted indices
            # Since the required number was already in the dict, it was found before the current number
            else:
                return [seen[required_num], index]
        