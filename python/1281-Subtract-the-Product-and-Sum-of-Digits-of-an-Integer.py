"""" https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [1,0]
        while n >= 1:
            arr[1] = arr[1] + (int(n)%10)
            arr[0] = arr[0] * (int(n)%10)
            n = int(n) / 10
        return(arr[0]-arr[1])

'''
Runtime: 28 ms, faster than 79.45% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
'''

