import heapq
class MedianFinder(object):
    # A naive approach (e.g., sorting the whole list each time) takes O(n log n) per median call — too slow for large data.
    # By definition the median: For an odd-length list: the middle number after sorting. For an even-length list: the average of the two middle numbers.
    # want to insert in log n time and retrieve the median in O(1) time 

    # data structure: Two Heaps: one max-heap and one min-heap
    # Left half (max-heap): stores the smaller numbers, with the largest at the top.
    # Right half (min-heap): stores the larger numbers, with the smallest at the top. This allows us to easily access the 

    # len(max_heap) == len(min_heap) if even number of elements and 
    #  len(max_heap) == len(min_heap) + 1 if odd number of elements so that we can computer: the top of max_heap (if odd), the average of tops of both heaps (if even)
    def __init__(self):
        # this is the max heap so invert the valids
        self.low = [] 
        self.high = []
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        '''
        Always insert into low
        Move one element to high to maintain order
        Rebalance if needed to maintain size
        '''
        # push into the max heap
        heapq.heappush(self.low, -num)

        # move the max of the left half into the right side (this is actually the smallest value since the map heap is negative)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # All numbers in low (max-heap) ≤ all numbers in high (min-heap) and # maintain size property: len(low) >= len(high) by one 
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        """
        :rtype: float
        """
        # top of the lower half in the max heap
        if len(self.low) > len(self.high):
            return -self.low[0]
        # average of the two since it a even lengthed list
        # have to use 2.0 otherwise it convert to int
        return (-self.low[0] + self.high[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()