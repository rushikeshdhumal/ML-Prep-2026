"""
Valid Anagram
https://neetcode.io/problems/is-anagram/question

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Intialize 2 dicts to store counts of each char
        s_counts = {}
        t_counts = {}

        # Base validation: The 2 arrays are not anagrams if they are not of the same length
        if len(s) != len(t):
            return False
        
        # Populating the count dicts with the value counts
        for i in s:
            s_counts[i] = s_counts.get(i, 0) + 1
        for j in t:
            t_counts[j] = t_counts.get(j, 0) + 1
        
        # Anagrams true only if the dicts are exactly the same
        if s_counts == t_counts:
            return True
        else:
            return False
        
    # Time: O(n+m) iterating over both lists of length n and m
    # Space: O(1) because the maximum length of the dicts will always be 26 (lowercase alphabet)