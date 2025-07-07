class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        def calc_water(left, right):
            return (right - left) * (min(height[left], height[right]))
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            max_area = max(max_area, calc_water(left, right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area