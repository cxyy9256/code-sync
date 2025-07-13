class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)

        # boolean DP array dp of length len(s) + 1, where: dp[i] is True if s[:i] (the first i characters) can be segmented
        dp = [False] * (len(s) + 1)

        dp[0] = True # since empty string is valid
        for i in range(1, len(s) + 1):
            for j in range(i):
                # You can only attach a new brick s[j:i] if the wall before j (s[0:j]) is already solid (dp[j] == True), like cannot cut in between words
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True

                    break
        return dp[len(s)]