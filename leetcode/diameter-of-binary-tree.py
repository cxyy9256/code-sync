# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_val = 0
        # It does not naturally share variables across all recursive levels unless: You return something up the call stack. Or use a nonlocal/global variable
        # self.max_diameter is an instance variable
        
        # So it persists across all recursive calls to dfs. This makes it ideal for tracking a max value that’s updated anywhere in the tree, not just returned from one leaf.
        
        def dfs(node):
            # nonlocal max_diameter
            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            self.max_val = max(self.max_val, left_len + right_len)
            return max(left_len, right_len) + 1
        
        dfs(root)
        return self.max_val