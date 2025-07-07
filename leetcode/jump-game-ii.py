class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        jumps = 0 
        farthest = 0
        current_end = 0 

        for i in range(len(nums) -1): # edge case of [1] is just 0 jumps
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
            if current_end >= len(nums)-1:
                break
        return jumps