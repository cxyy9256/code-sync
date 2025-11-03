class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        output = [[1]] 
        for row in range(1, numRows):
            dp = [1]
            for i in range(1, row):
                dp.append(output[row-1][i-1] + output[row-1][i])
            dp.append(1)
            output.append(dp)
        return output