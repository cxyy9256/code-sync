class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

        '''
        p_front = 0
        p_back = len(nums)-1
        while (p_back > p_front):
            if (nums[p_back] == val):
                p_back -= 1
            if (nums[p_front] == val):
                nums[p_front] = nums[p_back]
                nums[p_back] = val
            else:
                p_front += 1
        while (len(nums) > 0 and nums[-1] == val):
            nums.pop(-1)
        '''