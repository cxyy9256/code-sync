class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # de Bruijn sequence: sequence order n over an alphabet of size k is a  cyclic sequence in which every possible string of length n over that alphabet appears exactly once as a substring.
        # shortest possible sequence that covers all k^n substrings of length n.
        # Hierholzer’s algorithm.
        # directed graph : Node: A string of length n - 1
        # has edges k of them, Edge: You create an edge by appending one digit to the node
        
        '''
        de Bruijn sequence: the shortest string that contains every possible length-n string over digits 0 to k - 1.

This is done by walking through a graph:

Nodes = strings of length n - 1

Edges = strings of length n (formed by appending a digit)

Goal = visit every edge exactly once (Eulerian circuit)


        '''
        
        visited = set()
        
        # This list stores the digits used to construct the final de Bruijn sequence — but in reverse order.
        result = []
        
        # node is the length of n - 1 sequence
        def dfs(node):
            
            # You're looping through all possible digits in the alphabet [0, 1, ..., k - 1]. So if k = 2, you're trying digits 0, 1. You’re saying: “For the current node, let’s try adding each possible digit to form an edge.
            
            for digit in range(k):
                edge = node + str(digit)
                #
                if edge not in visited:
                    visited.add(edge)
                    # f edge = "010", then edge[1:] = "10" and then 10 is your new node
                    dfs(edge[1:])
                    # dd the digit to result after finishing that edge, but this digit should be first 
                    result.append(str(digit))
        
        # resutl has all the aditional nodes you need to add to me
        start = "0" * (n-1)
        dfs(start)
        # add to your original node
        return start + ''.join(reversed(result))