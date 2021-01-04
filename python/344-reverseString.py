"""" https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        """
        Do not return anything, modify s in-place instead.
        """

# test = Solution()
# print(test.reverseString(["h","e","l","l","o"]))
# print(test.reverseString(["H","a","n","n","a","h"]))

'''
Runtime: 184 ms, faster than 96.36% of Python3 online submissions for Reverse String.
'''

