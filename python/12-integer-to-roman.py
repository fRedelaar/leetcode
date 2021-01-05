"""" https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        stringer = ""

        # 1000 and 900
        while num > 999:
            stringer = stringer + 'M'
            num = num - 1000
        while num >= 900:
            stringer = stringer + 'CM'
            num = num - 900

        # 500 and 400
        while num > 499:
            stringer = stringer + 'D'
            num = num - 500
        while num >= 400:
            stringer = stringer + 'CD'
            num = num - 400

            # 100 and 90
        while num > 99:
            stringer = stringer + 'C'
            num = num - 100
        while num >= 90:
            stringer = stringer + 'XC'
            num = num - 90

            # 50 and 40
        while num > 49:
            stringer = stringer + 'L'
            num = num - 50
        while num >= 40:
            stringer = stringer + 'XL'
            num = num - 40

            # 10 and 9
        while num > 9:
            stringer = stringer + 'X'
            num = num - 10
        while num >= 9:
            stringer = stringer + 'IX'
            num = num - 9

            # 5 and 4
        while num > 4:
            stringer = stringer + 'V'
            num = num - 5
        while num == 4:
            stringer = stringer + 'IV'
            num = num - 4
        while num > 0:
            stringer = stringer + 'I'
            num = num - 1

        return stringer


'''
Runtime: 36 ms, faster than 98.11% of Python3 online submissions for Integer to Roman.
'''

