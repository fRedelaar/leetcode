"""" https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newlist = []
        for i in nums:
            newlist.append(i*i)
        newlist.sort()
        return(newlist)

'''
Runtime: 196 ms, faster than 98.54% of Python3 online submissions for Squares of a Sorted Array.
'''

