class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letters = {
                            "2": "abc",
                            "3": "def",
                            "4": "ghi", 
                            "5": "jkl", 
                            "6": "mno", 
                            "7": "pqrs", 
                            "8": "tuv", 
                            "9": "wxyz"
                        }
        # secodn test case
        if not digits:
            return []
        
        result = []
        
        # idx is what digit you are on, the path built so far
        def backtrack(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx+1, path + letter)
            
        backtrack(0, "")
        return result