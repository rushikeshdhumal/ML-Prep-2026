"""
Best Time to Buy and Sell Stock (Sliding Window)
https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initializing two pointers for the sliding window
        l = 0
        r = 0
        len_list = len(prices)
        # Storing the current and max profits
        current_prof = 0
        max_prof = 0

        # We start from both pointers at 0 and move the right pointer ahead till the end of the list
        while r < len_list:

            # If the price at the right is greater, we calculate the profit
            # We compare the current profit with the existing max profit and store the higher one
            # Then we move right pointer ahead to get the profit (if any) from the remaining prices
            if prices[r] >= prices[l]:
                current_prof = prices[r] - prices[l]
                max_prof = max(max_prof, current_prof)
                r += 1

            # when the right price is lower than left, it gives us a potential new, lower buying point.
            # we save the existing max profit before resetting to the new pointers' iteration
            # set the current profit to 0 for the new window
            # move the left pointer ahead to the right pointer's position
            else:
                max_prof = max(max_prof, current_prof)
                current_prof = 0
                l = r
        
        return max_prof

        