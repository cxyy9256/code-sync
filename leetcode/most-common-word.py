class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        # preprocess string - convert all the words into lowercase
        # make sure all the words are gapped by one space
        cleaned = ''
        for c in paragraph:
            # isalnum = is alphabetic or numeric
            if c.isalnum(): # if its alphabetic
                cleaned += c.lower()
            else:
                cleaned += " "
        
        words = cleaned.split() # an array with each of the words 
        
        # key = word (processed): number of time occured
        occurance = {}
        banned_set = set(banned) # lookup is O(1) instead of O(n)
        
        for word in words:
            if word not in banned_set:
                if word in occurance:
                    occurance[word] += 1
                else:
                    occurance[word] = 1
                    
                    
        # find word with max frequency
        max_word = ''
        max_count = 0
        for word in occurance:
            if occurance[word] > max_count:
                max_count = occurance[word]
                max_word = word
        return max_word