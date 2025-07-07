class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # topological order in a directed graph 
        
        # for each graph[i] has all the courses that depend on course i to take, i is the prereq
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses # in_degree[i] = number of prereq that course i has 
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
            
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        completed = 0
        while queue:
            course = queue.pop(0)
            completed += 1
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return completed == numCourses