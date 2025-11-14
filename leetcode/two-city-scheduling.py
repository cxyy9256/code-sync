class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        # sort by the difference, apprently in bloomberg interview
        costs.sort(key=lambda x: x[0] - x[1])

        target = n//2
        total = 0
        for i, (a, b) in enumerate(costs):
            if i < target:
                total += a
            else:
                total += b
        return total