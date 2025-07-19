class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # this question is so confusing
        # can approach using dp or recursion
        
        #  Define the DP Table
        # Let dp[i][j] be True if s[0:i] matches p[0:j]
        # Does the first i characters of string s match the first j characters of pattern p?

        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        # base case empty strings match 
        dp[0][0] = True

        # pattern matching an empty string (s): this only happens when you have something like a* or a*b*, 
        # s  = "", p is longer
        # want to go forward because we need to populate the cases of dp[0][4]
        for j in range(2, n+1):
            # the 
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2] # will fall back on base case dp[0][0]

        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # case 1: you have a . or its a direct match, you want to look at the previous state 
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1] 
                
                elif p[j-1] == '*':
                    # subcase 1: matches 0 of the preceding element
                    dp[i][j] = dp[i][j-2]
                    # subcase 2: One or more occurrences:
                    # the character before the * matches the character before in s
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]