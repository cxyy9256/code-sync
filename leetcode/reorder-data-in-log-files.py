class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            # identifier is a str, rest is a string
            identifier, rest = log.split(" ", 1) # split by the first of the spaces
            # check first character to see
            if rest[0].isalpha():
                letter_logs.append((identifier, rest, log))
            else:
                digit_logs.append(log)
                
        
        #print(letter_logs)
        #print(digit_logs)
        
        # sort by content then identifier
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        sorted_letter_logs = [log for _, _, log in letter_logs]
        
        return sorted_letter_logs + digit_logs