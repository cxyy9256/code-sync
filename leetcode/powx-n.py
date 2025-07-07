class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Multiply x by itself n times. - O(N) 

        def fastpower(x, n):
            if n == 0:
                return 1.0
            half = fastpower(x, n//2)
            if n % 2 == 0:
                return half * half 
            else: 
                return half * half * x # extra one because its odd

        if n < 0:
            x = 1 / x
            n = -n # turn the negative into positive

        return fastpower(x, n)