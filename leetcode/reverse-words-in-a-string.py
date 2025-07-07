class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        for i in range(len(words)//2):
            word = words[i]
            words[i] = words[len(words)-1 - i]
            words[len(words)-1 - i] = word
        return " ".join(words)