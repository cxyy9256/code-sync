# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        
        def get_height(node):
            h = 0
            
            while node:
                h += 1
                node = node.left
                
            return h
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        # The left subtree is perfect with height h So it has exactly 2^h - 1 nodes Add 1 for the root, the (1 << left_height) is 2^left_height
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right) # bc the right tree could be incomplete
        else:
            return (1 << right_height) + self.countNodes(root.left)