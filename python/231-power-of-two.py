"""" https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Example 4:
Input: n = 4
Output: true

Example 5:
Input: n = 5
Output: false
"""

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        if int(str(math.log2(n))[-1]) == 0:
            return True
        else:
            return False


'''
Runtime: 32 ms, faster than 63.99% of Python3 online submissions for Power of Two.
'''

