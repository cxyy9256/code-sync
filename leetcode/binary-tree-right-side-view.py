# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        '''
        A deque (pronounced "deck") is a double-ended queue. While a standard queue is a linear data structure following the FIFO (First-In, First-Out) principle, meaning elements are added at one end (rear) and removed from the other (front), a deque offers greater flexibility. It allows elements to be inserted and deleted from both the front and the rear. 
        '''
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size -1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result