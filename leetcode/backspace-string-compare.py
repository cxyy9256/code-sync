class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def process(string):
            stack = []
            for char in string:
                if char == "#":
                    if stack: # if its empty don't pop anything
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack) 
            
        
        return process(s) == process(t)