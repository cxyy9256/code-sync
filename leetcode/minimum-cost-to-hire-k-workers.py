class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        import heapq
        
        # All selected workers must be paid at the same wage-to-quality ratio, and this ratio must be at least what each worker demands.
        # Sort all workers by wage[i] / quality[i] (i.e., their minimum ratio required)
        workers = [(float(w) / q, q) for q, w in zip(quality, wage)]  # need the float otherwise there is rounding error
        workers = sorted(workers)
        
        heap = []
        total_quality = 0
        min_cost = float('inf') # be careful for 
        
        for ratio, q in workers:
            heapq.heappush(heap, -q) # Python’s built-in heapq module implements a min-heap by default.
            total_quality += q
            
            if len(heap) > k:
                removed_q = -heapq.heappop(heap)
                total_quality -= removed_q # pops the ones with lowest but since its -q its the highest quality
                
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
                # total cost = r × (smallest possible total quality) minimize the total quality of workers
        return min_cost