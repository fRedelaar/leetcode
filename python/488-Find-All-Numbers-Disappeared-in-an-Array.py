"""" https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        returnList = []
        length = len(nums) + 1
        nums = set(nums)

        for i in range(1, length):
            if i not in nums:
                returnList.append(i)

        return (returnList)

'''
Runtime: 312 ms, faster than 99.09% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''

