class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # map each of the string into an array [before ., after .]
        v1 = (map(int, version1.split(".")))
        v2 = (map(int, version2.split(".")))
        
        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            rev1 = v1[i] if i < len(v1) else 0 
            rev2 = v2[i] if i < len(v2) else 0
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0