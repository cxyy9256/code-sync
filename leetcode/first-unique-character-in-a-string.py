class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # map with {number: [list of indx that it occurs]}
        
        char_idx = {}
        
        for i, c in enumerate(s):
            if c in char_idx:
                char_idx[c].append(i)
            else:
                char_idx[c] = [i]
                
        # find the smallest idx from all the ones that are len 1 in the list
        # this is the first nonrepeating one bc we go in order
        for c in s:
            if len(char_idx[c]) == 1:
                return char_idx[c][0]
        
        return -1