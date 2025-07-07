class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Option 1: Min-Heap of Size k (O(n log k)) Use a heap of size k to keep track of the top k largest elements.
        
        import heapq
        
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # remove the smallest
            
        return min_heap[0] # smallest among the top k, which is the kth largest overall.