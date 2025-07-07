class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_len = 0 
        char_count = {}
        
        for right in range(len(s)):
            if s[right] not in char_count:
                char_count[s[right]] = 0
            char_count[s[right]] += 1
            
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
        
        return max_len