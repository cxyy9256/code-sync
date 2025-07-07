class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        
        curr_num = 0
        curr_str = ""
        
        for char in s:
            if char.isdigit():
                curr_num = 10 * curr_num + int(char)
            elif char == "[":
                stack.append((curr_str, curr_num)) # stores the old current formed string 
                curr_num = 0
                curr_str = ""
            elif char == "]":
                last_str, num = stack.pop()
                curr_str = last_str + curr_str * num       
            else:
                curr_str += char
        return curr_str