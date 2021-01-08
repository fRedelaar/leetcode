"""" https://leetcode.com/problems/to-lower-case/

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "he0re"
Output: "he0re"

Example 3:
Input: "L%VELY"
Output: "l%vely"
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

'''
Runtime: 32 ms, faster than 41.41% of Python3 online submissions for To Lower Case.'''

