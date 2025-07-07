class Solution:
    def maxProfit(self, prices):
        max_diff = 0 
        min_price = 1e5

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                max_diff = max(diff, max_diff)
        return max_diff