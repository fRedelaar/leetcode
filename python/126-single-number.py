"""" https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lib = {}

        for i in nums:
            if i in lib:
                lib[i] += 1
            else:
                lib[i] = 1
        sorted_d = sorted(lib.items(), key=operator.itemgetter(1))
        return (sorted_d[0][0])

'''
Runtime: 140 ms, faster than 41.34% of Python3 online submissions for Single Number.
'''

