# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0 
        stack = [(root, 0)]
        total_sum = 0
        while stack:
            node, current_sum = stack.pop()
            if node:
                current_sum = current_sum * 10 + node.val
                if not node.left and not node.right:
                    total_sum += current_sum
                if node.right:
                    stack.append((node.right, current_sum))
                if node.left:
                    stack.append((node.left, current_sum))
        return total_sum