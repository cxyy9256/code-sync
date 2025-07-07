class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        # reverse with 
        
        # u'...' prefix just means these are Unicode strings
        
        # s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
        # want to get soomethin  like [(2, u'cd', u'ffff'), (0, u'a', u'eee')]
        replacements = sorted(zip(indices, sources, targets), reverse=True)
        # print(replacements)
        
        for i, source, target in replacements:
            if s[i:i+len(source)] == source:
                s = s[:i] + target + s[i+len(source):]
        return s