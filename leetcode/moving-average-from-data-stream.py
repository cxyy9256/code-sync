class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size # how wide the window is maximum, could be not filled
        self.queue = []
        self.running_sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.running_sum += val

        # if the size of the queue exceeds the 
        if len(self.queue) > self.size:
            removed = self.queue.pop(0) # pop from the left
            self.running_sum -= removed

        return float(self.running_sum)/ len(self.queue) # not always the same size as the max_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)