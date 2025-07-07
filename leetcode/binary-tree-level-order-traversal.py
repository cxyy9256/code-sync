# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Breadth-first search (BFS) is a graph traversal algorithm that explores a graph layer by layer, starting from a designated root node. It visits all the node's immediate neighbors before moving on to the next level of neighbors,
        if not root:
            return []
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                # queue's FIFO (First-In, First-Out)
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level)
        
        return result