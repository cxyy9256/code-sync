class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # best approach is a binary search until you final smallest integer square who is less then x

        # x = 0 or 1
        # square root function is monotonic (increasing), 
        if x < 2:
            return x 
        
        left = 1
        right = x // 2 # sqrt(x) cannot be greater than x over 2

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            square = mid * mid

            if square == x:
                return mid # perfect square

            elif square < x:
                left = mid + 1
                print(left)
            
            else: # square > x
                right = mid - 1
        # when the loop exits left was greater than right
        # right is the last value that satisfied mid^2 ≤ x
        # left is the first value that failed, i.e. left^2 > x
        return right