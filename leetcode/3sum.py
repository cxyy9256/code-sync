class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sorting and two pointer strategy 
        nums.sort()
        n = len(nums)
        result = []
            
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # fix the thing at i 
            target = -nums[i]
            
            left, right = i+1, n -1
            
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
        return result