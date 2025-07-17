class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        #
        from collections import defaultdict
        # classic Union-Find (Disjoint Set Union) or a graph + DFS questions 

        # Nodes: Each email is a node. Edges: If two emails belong to the same account: it is adjacency list representing the email graph. so the Key: an email address (string) + Value: a list of emails (strings) that are directly connected to this one, that 
        graph = defaultdict(list)
        # email to the account holder's name. Key: an email address (string), Value: the name of the account (also a string)

        email_to_name = {}

        for account in accounts:
            name = account[0]
            # you could make fully connectred graph but we only need to add enough so that using DFS we can reach every other node, UNDIRECTED GRAPH KEEP IN MIND
            # first_email as a hub node, and connect every other email to it
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name
            
        # build dfs to find connected components

        visited = set()
        # the thing you want to output and append the connected parts into 
        merged_accounts = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                # email_to_name[email] is a string
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts