class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = {}

        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] not in char_count:
                char_count[s[right]] = 0
            char_count[s[right]] += 1
            
            # too many distinct characters
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len