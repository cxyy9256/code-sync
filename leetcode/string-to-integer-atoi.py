class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_min = -2**31
        int_max = 2**31 -1
        s = s.lstrip() # remove leading whitespace
        print(s)
        
        if not s:
            return 0 
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                result = 10*result + int(char)

            else:
                break
        result *= sign
        
        
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        return result