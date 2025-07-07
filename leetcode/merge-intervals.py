class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort them by first element since they could overlap 
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # merged empty of range doesn't intersect
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # ranges intersect
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged