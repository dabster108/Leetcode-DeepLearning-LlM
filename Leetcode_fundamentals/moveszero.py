#move zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Do not return anything, modify nums in-place instead.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        print(nums)  

        '''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0  

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
        
        print(nums)
