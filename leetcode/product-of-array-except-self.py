class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # algorithm is keep two arrays one with the left product of index i and the right product of i
        
        length = len(nums)
        output = [1] * length
        
        # left product
        
        for i in range(1, length):
            output[i] = nums[i-1] * output[i-1] # almost like recursive
            
        # right product 
        prod = 1
        for i in range(length-1, -1, -1):
            output[i] = output[i] * prod
            prod *= nums[i] # so that it can be used in the next index 
        return output