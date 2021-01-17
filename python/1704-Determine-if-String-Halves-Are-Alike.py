"""" https://leetcode.com/problems/determine-if-string-halves-are-alike/

You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters. Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:
Input: s = "MerryChristmas"
Output: false

Example 4:
Input: s = "AbCdEfGh"
Output: true

Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        stringer = "aeiou"
        counter1 = counter2 = 0
        length = len(s) / 2
        str1 = s[:int(length)].lower()
        str2 = s[int(length):].lower()

        for letter in str1:
            if letter in stringer:
                counter1 += 1

        for letter in str2:
            if letter in stringer:
                counter2 += 1

        if counter1 == counter2:
            return True
        else:
            return False



#Second solutions using dictionaries

# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         counter1 = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#         counter2 = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#         length = len(s) / 2
#         str1 = s[:int(length)].lower()
#         str2 = s[int(length):].lower()
#
#         for letter in str1:
#             if letter in counter1:
#                 counter1[letter] += 1
#
#         for letter in str2:
#             if letter in counter2:
#                 counter2[letter] += 1
#
#         countertje = counter1["a"] + counter1["e"] + counter1["i"] + counter1["o"] + counter1["u"]
#         countertje2 = counter2["a"] + counter2["e"] + counter2["i"] + counter2["o"] + counter2["u"]
#
#         if countertje == countertje2:
#             return True
#         else:
#             return False


'''
Runtime: 40 ms, faster than 38.50% of Python3 online submissions for Determine if String Halves Are Alike.
'''

