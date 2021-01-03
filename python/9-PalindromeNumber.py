"""" https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        new = ''

        if len(str(x)) == 1:
            return True
        if x < 0:
            return False

        for a in range(0, int(len(str(x)) / 2)):
            new = str(new) + str(temp % 10)
            temp = int(temp / 10)

        if len(str(temp)) > len(str(new)):
            temp = int(temp / 10)

        if int(new) == int(temp):
            return True
        else:
            return False

'''
Runtime: 72 ms, faster than 33.18% of Python3 online submissions for Palindrome Number.
'''
