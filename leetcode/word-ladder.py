class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        # convert wordList into a set because lookup is faster
        wordSet = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            # pop the word with current step 
            word, steps = queue.popleft()
            print((word, steps))
            
            if word == endWord:
                return steps
            
            # for each position in the word try the 26 replacements for each position
            # if new word is in position add to queue, remove from word list
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append([next_word, steps+1])
        return 0