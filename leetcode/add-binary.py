class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # bit manipulation approach
        # int(a, 2) converts the binary string a into an integer (base-2).
        x, y = int(a, 2), int(b, 2)

        while y:
            # ^ is the bitwise XOR operator. It adds bits without carrying:
            answer = x ^ y #

            '''
            & is bitwise AND: it detects where both x and y have 1s → that's where you need to carry.

        << 1 means shift left by 1 (carry moves one position left, just like decimal addition: carry to next digit).
            '''
            carry = (x & y) << 1
            x, y = answer, carry
        
        # bin(x) converts the final integer result to a binary string, [2:] slices off the '0b' prefix, returning only the binary digits.
        return bin(x)[2:]