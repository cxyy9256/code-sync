class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_pos = points[0][1]
        for start, end in points:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
        return arrows