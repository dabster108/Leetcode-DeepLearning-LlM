//rotate an array of n elements to the right by k steps.
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Note:
# Try to come up with as many solutions as you can, there are at least 3 different ways to solve this problem.
# Do not use the built-in array method.
# Example:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n  
        
       
        nums[:] = nums[::-1]
        
      
        nums[:k] = nums[:k][::-1]
        
       
        nums[k:] = nums[k:][::-1]
