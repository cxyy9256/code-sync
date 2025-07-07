class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        max_dist = 0
        last = -1 # last seen person:
        
        for i in range(n):
            if seats[i] == 1:
                # alex can sit in first seat and be far away from the other ppl 
                if last == -1:
                    max_dist = i
                    
                # middle part , max distance is in right between two 1's 
                else:
                    dist = (i-last)//2
                    max_dist = max(max_dist , dist)
                    
                last = i
                
        # n - 1 is the index of the last seat., last is the index of the last person (1) encountered in the loop. this is distance Alex would have from the last person if he chose the final seat.
        max_dist = max(max_dist, n - 1 - last)
        return max_dist