class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_digit_squared(num):
            return sum(int(digit)**2 for digit in str(n))
        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = sum_digit_squared(n)
        
        return n == 1