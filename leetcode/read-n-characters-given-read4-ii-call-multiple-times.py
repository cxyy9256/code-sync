# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    
    def __init__(self):
        # store left over characters from previous read4 calls
        self.temp = [''] * 4
        self.buffer_pt = 0
        self.buffer_max = 0 # number of characters in buffer at the moment
    
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        
        total = 0
        
        temp = [''] * 4
        
        while total < n:
            # buffer is empty, call read4
            if self.buffer_pt == self.buffer_max:
                self.buffer_max = read4(self.temp)
                self.buffer_pt = 0
                
                if self.buffer_max == 0:
                    break
                
            while self.buffer_pt < self.buffer_max and total< n:
                buf[total] = self.temp[self.buffer_pt]
                total += 1
                self.buffer_pt += 1
        
        return total