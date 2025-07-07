class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # problem is best modeled as a graph, where each variable is a node, and each equation like A / B = value becomes a directed edge
        
        # A → B with weight = value
        # B → A with weight = 1 / value
        
        # default dict is just good because it fills in the default thing even if its empty of he key doesn't exist yet
        from collections import defaultdict
        
        
        # for each new query, you cna do dfs and multiply the weights along the way to get the answer otherwise return -1
        graph = defaultdict(dict) # graph[a][b]  = val # the weight from one edge to another
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1/val
            
        '''
        {
          "a": {"b": 2.0},
          "b": {"a": 0.5, "c": 3.0},
          "c": {"b": 1/3.0}
        }
        '''
        print()
            
        # current = [a][b] some sort of node and then target is 
        # current is an index
        def dfs(current, target, visited):
            
            # base cases
            if current not in graph or target not in graph:
                return -1.0
            if current == target:
                return 1.0
            
            visited.add(current)
            
            # format of graph above [("a", 0.5), ("c", 3.0)]
            for neighbor, val in graph[current].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    return result * val
            return -1.0
                
            
        
        results = []
        
        # queries = [['a', 'b'], ['b', 'c']], you can just unpack it with for a, b. in queries is the same as for pair in queries:, then a = pair[0], b = pair[1]
        for a, b in queries:
            results.append(dfs(a, b, set()))
            
        return results