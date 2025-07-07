# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = -1e9
        
        def max_gain(node):
            
            if not node:
                return 0
            
            left_gain = max(max_gain(node.left), 0)
            print(left_gain)
            right_gain = max(max_gain(node.right), 0)
        
            
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
            
            return node.val + max(left_gain, right_gain) # for the recursion return back to parent
        
        max_gain(root)
        return self.max_sum