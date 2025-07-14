class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # ensure that s is shorter than t just so that we can compare if one is in the next check of length 
        if len(t) < len(s):
            s, t = t, s

        if len(t) - len(s) > 1:
            return False

        # insert and delete is the same thing if you reverse the length of the shortest and the longest 

        for i in range(len(s)):
            if s[i] != t[i]:
            # Case 1: replace (same length)
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
            # case 2: insert but we know that t is longer, outside the loop
                return s[i:] == t[i+1:]
        return len(t) == len(s) + 1