"""" https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        return int((x ** 0.5))

test = Solution()
print(test.mySqrt(4))
print(test.mySqrt(8))
print(test.mySqrt(9))



'''
Runtime: 28 ms, faster than 93.68% of Python3 online submissions for Sqrt(x).
'''

