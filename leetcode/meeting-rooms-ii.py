class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import heapq
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        heap = []
        heapq.heappush(heap, intervals[0][1]) # initialize with the end time of the first meeting
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # room is free remove the earliest meeting
            if start >= heap[0]:
                heapq.heappop(heap)
                
            heapq.heappush(heap, end)
        return len(heap) # means 2, x num of meetings are overlapping at some point → need 2 rooms.