class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Step 1: BFS to build the graph of shortest paths, most important is to build a good graph that isn't redundent with level
        from collections import deque, defaultdict
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # graph {key = word: [ list of words that are reachable froom that word in the same current bfs depth - Only include words found the first time at that BFS level.]}
        # we want to create a reverse graph for optimization purposes 
        # so if we have "hot" → "dot", "lot" we add reverse_graph["dot"] = ["hot"] and reverse_graph["lot"] = ["hot"]
        reverse_graph = defaultdict(list)
        #  set of words at the current BFS level.
        level = {beginWord}
        visited = set()
        found = False

        while level and not found:
            next_level = set()
            for word in level:
                visited.add(word)
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            reverse_graph[new_word].append(word) # reversed edge  
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)

            level = next_level

        #if not found:
            #return []
        # Step 2: Backtrack (DFS) from endword to beginword by using the reversed graph we made above
        result = []
        # word is the current word you are on and starting with
        def dfs(path, word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for prev in reverse_graph[word]:
                dfs(path + [prev], prev)
        

        dfs([endWord], endWord)
        return result

        # this is faster than original solution in the DFS forward, Explores many paths trying to reach endWord
        # Forward DFS from hit has to explore every path until it finds cog. Even if you use BFS to build the graph, your DFS might wander down many forward paths that don’t lead to cog, especially when the graph is large or dense.
        # You never explore invalid or dead-end paths (no wasted DFS branches)
        # foward one you explore a lot of waster branches

        # if wordlist was wordList = ["hot","dot","dog","lot","log","cog", "hog", "bog", "pog"]
        '''
 you would explore this
        hit → hot → dot → dog → hog 
        hit → hot → dot → bog 

        hit → hot → lot → log → pog 
        '''