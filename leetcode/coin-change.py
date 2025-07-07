class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] = minimum amount of coins to make the value i 
        
        # base case is dp[0] = 0
        # So we need indices from 0 up to amount, inclusive, which is why its amount + 1
        dp = [float('inf')] * (amount + 1)
    
        
        dp[0] = 0
        for coin in coins:
            # For each coin denomination, We try to use this coin to improve the solution to each sub-amount.
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
            
            
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1