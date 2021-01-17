"""" https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Example 3:
Input: n = 2331
Output: 880
"""
import math
import timeit

start = timeit.default_timer()


class Solution:
    def trailingZeroes(self, n: int) -> int:
        min = -1
        a = math.factorial(n)

        while str(a)[min] == '0':
            min -= 1

        return (min*-1 -1)

test = Solution()
digits = 2465
print(test.trailingZeroes(digits))
stop = timeit.default_timer()

print('Time: ', stop - start)

'''
Status: Time Limit Exceeded
'''

