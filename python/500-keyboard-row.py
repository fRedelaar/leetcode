"""" https://leetcode.com/problems/keyboard-row/

Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below.

https://assets.leetcode.com/uploads/2018/10/12/keyboard.png

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        row1op = row2op = row3op = 0
        returnList = []

        for i in words:
            for letter in i:
                length = len(i)
                if letter in row1:
                    row1op = row1op + 1
                elif letter in row2:
                    row2op = row2op + 1
                elif letter in row3:
                    row3op = row3op + 1
            if length == row1op or length == row2op or length == row3op:
                returnList.append(str(i))
            row1op = row2op = row3op = 0

        return(returnList)

test = Solution()
a = ["Hello", "Alaska", "Dad", "Peace"]
print(test.findWords(a))


'''
Runtime: 24 ms, faster than 93.78% of Python3 online submissions for Keyboard Row.
'''

