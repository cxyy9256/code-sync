class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0 
        
        # sliding window algorithm
        start = 0
        current_sum = 0 
        min_len = float('inf')
        for end in range(len(nums)):
            current_sum += nums[end]
            # >= bc you save that one case that work, even if future don't
            while current_sum >= target: 
                min_len = min(min_len, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_len