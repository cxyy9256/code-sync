class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp problems - memoization
        # O (n * amount)
        n = len(coins)
        dp = [0] * (amount +1)
        dp[0] = 1
        for i in range(n-1, -1, -1):
            # we are taking 
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]