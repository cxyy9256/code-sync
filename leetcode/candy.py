class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        # left pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # right pass 
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j], candies[j+1] + 1)

        return sum(candies)