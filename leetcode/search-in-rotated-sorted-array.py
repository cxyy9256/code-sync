class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > nums[n-1]:
                left = mid + 1
            # pivot is to the right of mid
            else:
                right = mid - 1
        # when left == right that is the pivot

        # binary search over each of the two halves

        def binarySearch(left_bound, right_bound, target):
            left, right = left_bound, right_bound

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        
        answer = binarySearch(0, left -1, target)
        if answer != -1:
            return answer
        return binarySearch(left, len(nums)-1, target)