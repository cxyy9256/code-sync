# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.prev = None
        self.min_diff = float('inf')
        # inorder sorts it from smallest to 
        def inorder(node):
            if not node:
                return
            # traverse left tree
            inorder(node.left)

            # process the current node, self.prev holds the previous value in sorted list
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            # process right node
            inorder(node.right)
        inorder(root)
        return self.min_diff