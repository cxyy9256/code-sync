class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # sliding window algorithms O(n) which is better
        
        # mapping each unique character to its last seen occurance index
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                # move the left point past the last occurance
                left = char_map[s[right]] + 1
            
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len