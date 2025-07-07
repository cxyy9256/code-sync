class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # If you sell immediately at a higher price and then buy again later at a lower price, the sum of individual profits will always equal or exceed the profit you would get by waiting for a higher peak
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit