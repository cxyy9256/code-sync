class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [point for (dist, point) in heap]