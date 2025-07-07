class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        ransom_count = {}
        magazine_count = {}

        for char in ransomNote:
            ransom_count[char] = ransom_count.get(char, 0) + 1
        
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1
        
        for char in ransom_count:
            if magazine_count.get(char, 0) < ransom_count[char]:
                return False
        return True