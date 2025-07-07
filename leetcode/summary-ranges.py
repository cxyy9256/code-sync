class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if not nums:
            return nums
        results = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # len of previous part was just one
                if start == nums[i-1]: 
                    results.append(str(start))
                else:      
                    results.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        # take care of the last range
        if start == nums[-1]:
            results.append(str(start))
        else: 
            results.append(f"{start}->{nums[-1]}")
        return results