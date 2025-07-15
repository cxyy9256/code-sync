class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """

        def isIPv4(IP):
            # return array ["x1", x2, x3, x4]
            parts = IP.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                # the weird @ symbol case
                if not part.isdigit():
                    return False

                # check range, make sure to parse as int otherwise it always fails
                if not 0 <= int(part) <= 255:
                    return False
                # change leading 0's
                if str(int(part)) != part:

                    return False
            return True
    
        def isIPv6(IP):
            parts = IP.split(":")
            if len(parts) != 8:
                return False
            
            valid_digits = '0123456789abcdefABCDEF'
            for part in parts:
                if not (1<= len(part) <= 4):
                    return False
                for char in part:
                    if char not in valid_digits:
                        return False
            return True
        
        if isIPv4(queryIP):
            return "IPv4"
        elif isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"