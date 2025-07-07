class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        
        results = []
        prev = lower -1 
        
        for i in range(len(nums)+1):
            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper + 1
            
            if curr - prev > 1:
                results.append([prev +1, curr -1])
            
            prev = curr
        return results