class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first number always unique
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Whenever a new unique value is found at nums[i], it is copied forward into position j.
                nums[j] = nums[i]
                j += 1
        return j