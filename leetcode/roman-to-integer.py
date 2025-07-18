class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100,'D': 500, 'M': 1000}
        
        total = 0 
        prev_val = 0
        
        # reverse if roman to in
        for char in reversed(s):
            val = roman_map[char]
            if val < prev_val:
                # this means its one of those IV cases
                total -= val
            else:
                total += val
                prev_val = val
        return total