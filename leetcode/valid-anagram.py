class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = {}
        t_count = {}

        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        for char in s_count:
            if t_count.get(char, 0) != s_count[char]:
                return False
        for char in t_count:
            if s_count.get(char, 0) != t_count[char]:
                return False
        return True