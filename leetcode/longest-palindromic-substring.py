class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # don't need to check weird cases since s is always len greater than 1
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left -1 # next index when you exit the loop is two wrong letters 

        longest = 0
        start = 0 # where the best palindrome begins
        end = 0 # where the best palindrom ends
        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i+1)
            print("indx", i)
            print("len1", len1)
            print("len2", len2)

            longest = max(len1, len2)

            # updates the start and end indices of the longest palindrome substring found so far, based on, longer then current length 
            if longest > end - start + 1:
                # Even-length palindromes, it shifts left slightly to make room for the double-center, need to shift the left index a bit 
                start = i - (longest - 1)//2 
                end = i + (longest)//2
                print("start", start)
                print("end", end)
        return s[start:end+1]