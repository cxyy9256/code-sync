class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        mapping = {')': '(', '}':'{', ']': '['}
        
        for char in s:
            if char in mapping:
                if stack:
                    top = stack.pop()
                else:
                    top = "#"
                    
                if mapping[char] != top:
                    return False
                
            else:
                stack.append(char)
                
        return not stack # stack is empty is