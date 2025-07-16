class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # build a directed graph, 
        # 3 steps
        # extracting the dependency rules from input so taht a letter has to come before antoher one
        #  put the dependency into a graph (ke)
        # topological sort with bfs

        from collections import defaultdict, Counter, deque

        # default dict (set) = it automatically creates that key and assigns an empty set as its default value
        # it contains the key which is the node and the set is the list of edges that are OUTGOING FROM THAT NODE (SO THAT NODE IS AHEAD OF THE STUFF IN THE LIST)
        # IN DEGREE IS THE COUNTER THAT COUNTS THE NUMBER OF DEPENDENCIES OR THINGS IT NEEDS TO PASS FIRST TO USE THAT NODE
        # KEY IDEA: Where two words are adjacent, we need to look for the first difference between them. That difference tells us the relative order between two letters. Let's have a look at all the relations we can find by comparing adjacent words.

        adj_list = defaultdict(set)
        # in degree for all the number of characters
        in_degree = Counter({c: 0 for word in words for c in word})
        for word1, word2 in zip(words, words[1:]):
            for char_w1, char_w2 in zip(word1, word2):
                # if the two characters are teh same we have to move to the next two characters
                if char_w1 != char_w2:
                    if char_w2 not in adj_list[char_w1]:
                        # char_w1 has to come before char_w2
                        adj_list[char_w1].add(char_w2)
                        in_degree[char_w2] += 1
                    # don't need to check the rest of the word, breaks out of for loops and just goes to the next work pair
                    break
            else:
                # all the characters have matched so far
                # it's an unresolvable contradiction assumption from normal alphabet that spaces take precedent over and so there is no answer so valid ordering so ""
                # second word is a prefix of the 
                if len(word2) < len(word1):
                    return ""
            
        # step 2: pick off the nodes with in_degree - like the course schedule II problem, right now the order id c-> d in the solutions
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            char = queue.popleft()
            output.append(char)
            # already added to final list so there is one list prereq thing
            for dependent in adj_list[char]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
            
        # if not all the letters are in the output - there was a cycle so no valid ordering
        if len(output) < len(in_degree):
            return ""

        # convert the answer to a string
        return "".join(output)