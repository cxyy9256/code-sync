class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # topological order in a directed graph 
        # This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
        #  A topological ordering of a directed graph G is a labelling f of G's nodes such that: The f(v)'s are the set {1, 2, ..., n} and all the paris in G are going in forward order
        # courses in undergraduate major - sequence to take it
        # if g has a directed cycle, no topological ordering, no directed cycle  - can compute topological ordering
        # sink vertices - are the last ones
        
        graph = [[] for i in range(numCourses)] # graph[i] has all the courses that depend on course i
        in_degree = [0] * numCourses # in_degree[i] = number of prereq that course i has 
        
        for dest, prereq in prerequisites:
            graph[prereq].append(dest) # For example, if prerequisites = [[1, 0]], then: graph = [[1], []] → course 0 points to 1
            in_degree[dest] += 1 # has a prereq
            
    
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        order = []
        # bfs algorithm 
        while queue:
            course = queue.pop(0)
            order.append(course)
            # all the neighbors depend on this as a prereq
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # add the ones that can be in the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == numCourses:
            return order
        else:
            return [] # there is a cycle