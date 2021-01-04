""""https://leetcode.com/problems/plus-one/

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 """

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = digits

        length = len(digits)

        if temp[-1] == 9:
            if len(digits) == 4:
                temp[-1] = 0
                temp[-2] = temp[-2] + 1
                if temp[-2] == 10:
                    temp[-2] = 0
                    temp[-3] = temp[-3] + 1
                    if temp[-3] == 10:
                        temp[-3] = 0
                        temp[-4] = temp[-4] + 1
                    if temp[-4] == 10:
                        temp[-4] = 0
                        temp.insert(0, 1)

            if len(digits) == 3:
                temp[-1] = 0
                temp[-2] = temp[-2] + 1
                if temp[-2] == 10:
                    temp[-2] = 0
                    temp[-3] = temp[-3] + 1
                    if temp[-3] == 10:
                        temp[-3] = 0
                        temp.insert(0, 1)

            if len(digits) == 2:
                temp[-2] = temp[-2] + 1
                temp[-1] = 0
                if temp[-2] == 10:
                    temp[-2] = 0
                    temp.insert(0, 1)

            if len(digits) == 1:
                temp.insert(0, 1)
                temp[-1] = 0
        else:
            temp[-1] = temp[-1] + 1
        return temp

test = Solution()
digits = [1,2,3]
print(test.plusOne(digits))