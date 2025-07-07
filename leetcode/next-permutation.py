class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        
        # first decreasing term from the right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # find the smallest number to the right of the breaking points 
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            nums[i], nums[j] = nums[j], nums[i]   
        
        # reverse all the remaining stuff because it is in decreasing order 
        left, right = i+1, len(nums) -1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1