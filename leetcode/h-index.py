class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h_idx = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h_idx = i+1
            else:
                break
        return h_idx