class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum = 0
        # dictionary (hashmap) that keeps track of how many times each prefix sum has appeared as we iterate through the array.
        prefix_count = {0:1} # keeps track of how often a sum has occured initialize as 0: 1 since the sum of 0 has occured once
        result = 0

        
        for num in nums:
            current_sum += num
            if (current_sum -k) in prefix_count:
                result += prefix_count[current_sum -k]
            
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return result