class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        n = len(nums)
        closest = float('inf')
        
        for i in range(n-2): # fix the first number
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest-target):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
        return closest