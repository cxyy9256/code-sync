class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # bfs problem
        from collections import deque 
        def is_valid(string):
            # count the number of un matched parenthesis the open ( type
            open_val = 0
            for char in string:
                if char == "(":
                    open_val += 1
                elif char == ")":
                    open_val -= 1
                    # we have an extra ) here
                    if open_val < 0:
                        return False
            return open_val == 0
        
        results = []
        visited = set()
        queue = deque([s])
        found = False

        while queue:
            current = queue.popleft()
            if is_valid(current):
                results.append(current)
                found = True
            # this level around found don't go into a deeper level since we could potentially remove most of the brackets and come down to say 2 brackets () in the end which form a valid expression, u didn't remove the minimum amount tho 
            if found: 
                continue

            for i in range(len(current)):
                # its like a letter or smth so it can't be removed
                if current[i] not in ['(', ')']:
                    continue
                new_str = current[:i] + current[i+1:] # removing the parenthesis at index i to test
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)
        return results