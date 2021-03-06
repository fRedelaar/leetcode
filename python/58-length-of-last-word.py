"""" https://leetcode.com/problems/length-of-last-word/

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        if len(l) == 0:
            return 0
        return len(l[-1])
'''
Runtime: 24 ms, faster than 93.52% of Python3 online submissions for Length of Last Word.
'''

