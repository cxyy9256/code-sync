class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000. - One Hundred Twenty Three Thousand
        
        if num == 0:
            return "Zero"
        under_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                "Eighty", "Ninety"]
                
        thousands = ["", "Thousand", "Million", "Billion"]
                
        # returns for numbers under 1000
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return under_20[num] + " "
            elif num < 100:
                return tens[num//10] + " " + helper(num%10)
            else:
                return under_20[num//100] + " Hundred " + helper(num%100)
        
        # testing to make sure help function works
        # print(helper(999)) 
        # main loop
        
        res = ""
        
        i = 0
        while num > 0:
            # process last 3 digits at a time from right to left
            curr = num % 1000
            if curr != 0: # skips the 000 chunks prevents printing "Zero Thousand"
                # BE SUPER CAREFUL ABOUT EXTRA SPACE
                res = helper(curr) + thousands[i] + " " + res 
                # always prepending the newly processed chunk in front of the existing result string
            num //= 1000 # Remove the last 3 digits.
            i+= 1
        # strip() function removes any leading or trailing whitespace from the final result string because the help function will add a trailing space to the end
        return res.strip()