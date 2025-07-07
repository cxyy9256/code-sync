# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # the node in final traversal
        self.prev = None
        def helper(node):
            if not node:
                return
            
            # Perform a reverse post-order traversal (right -> left -> root)
            helper(node.right)
            helper(node.left)
            
            # Update the current node
            node.right = self.prev  # Link current node to the previous node
            node.left = None       # Remove the left link
            self.prev = node       # Update the previous node pointer
        
        helper(root)