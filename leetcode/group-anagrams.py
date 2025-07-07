class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hashmap {sorted word: [list of the anagrams of that word]}
        
        anagram_map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = [word]
            else: # key is already in the map
                anagram_map[key].append(word)
                
        output = []
        for key in anagram_map:
            output.append(anagram_map[key])
            
        return output