"""" https://leetcode.com/problems/self-dividing-numbers/

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        returnList = []
        for i in range(left, right+1):
            if len(str(i)) > 1:
                if '0' in str(i):
                    continue

            boolA = True
            for x in str(i):
                if int(i) % int(x) != 0:
                    boolA = False
            if boolA == True:
                returnList.append(i)

        return returnList

'''
Runtime: 72 ms. Your runtime beats 15.27 % of python3 submissions.
'''

