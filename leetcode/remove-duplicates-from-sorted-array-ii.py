class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            count = 1 
            while (j+1 < len(nums) and nums[j] == nums[j+1]):
                count += 1
                j += 1
            for k in range(min(2, count)):
                nums[i] = nums[j]
                i += 1
            j+=1
        return i