class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        # what number of characters you need from t
        need = {}
        
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        # track what we currently have
        window = {}
        have = 0
        result = ""
        res_len = 1e99
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            
            # character matches the exact count needed for that one
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == len(need):
                if (right - left + 1) < res_len:
                    result = s[left:right+1]
                    res_len = right - left + 1
                    
                # shrink the window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
                
        return result