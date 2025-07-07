# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_mirror(left, right):
            # both nodes are None, it means they mirror each other as "empty branches"
            # if left is none and right is none
            if not left and not right:
                return True
            
            # left is None right exists or left exists and right is none (return false): 
            if not left or not right:
                return False
            return (left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)