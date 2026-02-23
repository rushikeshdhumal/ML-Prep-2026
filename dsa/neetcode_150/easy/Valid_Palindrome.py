"""
Valid Palindrome
https://neetcode.io/problems/is-palindrome/question

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strip all non-alphanumeric chars from the string using isalnum()
        clean_s = ''.join([char for char in s if char.isalnum()])
        
        # Convert string to lower for given constraints
        clean_s = clean_s.lower()

        # Iterate and compare the first and last chars simultaneously
        for i in range(len(clean_s)):
            if clean_s[i] != clean_s[len(clean_s) - i - 1]:
                return False
            else:
                continue
        return True
    
     # Time complexity: O(n) where n is the length of the input string s
     # Space complexity: O(n) due to the creation of the clean_s string which can
        
"""
Optimal solution with O(n) time complexity and O(1) space complexity:

# Using 2 pointers left and right
l, r = 0, len(s) - 1

# Simultaneously moving left pointer forward and right pointer backward
while l < r:
    while l < r and not self.alphaNum(s[l]):
        l += 1
    while r > l and not self.alphaNum(s[r]):
        r -= 1
    if s[l].lower() != s[r].lower():
        return False
    l, r = l + 1, r - 1
return True

# Python ord() function is a built-in utility that returns
# the Unicode code point (an integer) for a given single character
# chr() function converts an integer code point back into a character.

def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
"""
        