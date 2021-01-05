"""" https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""

class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        new = ''

        if x < 0:
            temp = x * -1
            for a in range(0, int(len(str(x)))):
                new = str(new) + str(temp % 10)
                temp = int(temp / 10)
            new = int(new) / 10
            new = new * -1

        else:
            for a in range(0, int(len(str(x)))):
                new = str(new) + str(temp % 10)
                temp = int(temp / 10)

        if len(str(new)) > 1:
            while str(new)[0] == '0':  # to remove zeros when flipped around
                new = new[1:]

        if int(new) > 2147483647 or int(new) < -2147483647:
            new = 0

        return int(new)

'''
Runtime: 28 ms, faster than 87.82% of Python3 online submissions for Reverse Integer.
'''

