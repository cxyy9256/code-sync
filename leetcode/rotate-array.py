class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        '''
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)      # Step 1: Reverse the entire array
        reverse(0, k - 1)      # Step 2: Reverse the first k elements
        reverse(k, n - 1)      # Step 3: Reverse the rest
        '''
        '''
        n = len(nums)
        k = k % n
        count = 0  # Tracks the number of elements rotated

        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:  # If we complete a cycle
                    break
            start += 1
        '''