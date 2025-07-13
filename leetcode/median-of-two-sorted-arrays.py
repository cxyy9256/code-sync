class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # if you partition each of the arrays
        # key trick is to think of the merged array split into two halves:
        # instead of merging, we simulate this split by partitioning both arrays at positions i and j such that the total left side has (m + n) // 2 elements.
        
        # max(nums1_left, nums2_left) <= min(nums1_right, nums2_right)
        
        # we do binary search on nums1 (the left partition position i) nums 1 has to be the smaller array
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        len1, len2 = len(nums1), len(nums2)
        total = (len1 + len2)

        half = (total + 1) // 2

        left, right = 0, len1
        while left <= right:
            # We choose a partition i in nums1, which means we choose j = half - i in nums2, left side of the combined array has half elements
            i = (left + right) //2
            j = half - i

            '''
            a_left: last element on the left of nums1

            a_right: first element on the right of nums1

            b_left: last element on the left of nums2

            b_right: first element on the right of nums2
            '''

            a_left = float('-inf') if i == 0 else nums1[i-1]
            a_right = float('inf') if i == len1 else nums1[i]

            b_left = float('-inf') if j == 0 else nums2[j-1]
            b_right = float('inf') if j == len2 else nums2[j]

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
                else:
                    return max(a_left, b_left)

            # max of a_left should be in larger half, need to decrease the amount coming from num1 array
            elif a_left > b_right:
                right = i-1
            else:
                left = i+1