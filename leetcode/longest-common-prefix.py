class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        prefix_len = len(prefix)
        for string in strs[1:]:
            while string[0:prefix_len] != prefix:
                prefix = prefix[:-1]
                prefix_len -= 1
            if prefix_len == 0:
                return ""
        return prefix