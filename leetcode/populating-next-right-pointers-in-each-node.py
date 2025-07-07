"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # You can use recursion — the call stack doesn’t count as "extra space"
        # queue for bfs takes O(n) space
        # you know that both children 
        # Once you reach a leaf which is root.left, there's no more work to do
        if not root or not root.left:
            return root

        # If you just return without a value, Python implicitly returns None. That means when the recursive call returns, the parent call gets None — even though the tree itself was modified in place

        # All .next pointers are set to None. Your job is to populate those .next pointers level by level.

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        return root