class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force = O(n^3)
        # binary search  = O (n^2 log n)

        nums.sort() # O(nlogn)
        count = 0
        # need c< a+ b
        for i in range(len(nums) -1, 1, -1):
            start = 0
            end = i-1
            while start < end:
                # c = nums[i]
                if nums[start] + nums[end] > nums[i]:
                    count += end - start
                    end -= 1
                else:
                    start += 1
        return count