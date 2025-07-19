class Codec:
    # Common Approach: Length-prefixed Encoding for ["hello", "world"]
    5#hello5#world

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join("{}#{}".format(len(s), s) for s in strs)
        # for python 3.6 or later return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            result.append(s[i:i+length])
            i += length


        return result

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))