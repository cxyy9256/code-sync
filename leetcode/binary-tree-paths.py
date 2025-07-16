# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []

        result = []
        # Follow a path deeply from root to leaf before starting another which is why we do dfs not bfs.

        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->"+str(node.left.val))
            if node.right:
                dfs(node.right, path + "->"+ str(node.right.val))

        dfs(root, str(root.val))
        return result