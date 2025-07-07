# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # move prev one before the left position to connect the new reversed string at end 
        for i in range(left-1):
            prev = prev.next
        
        # creating the new reversed section
        current = prev.next
        next_node = None
        for i in range(right-left+1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp
        
        # prev.next points to the original left node (which is now the tail of the reversed segment).
        # current points to the first node after the reversed segment.
        # connects the tail of the reversed segment (original left node) to the rest of the list (node at position right + 1).
        # next_node is at the beginning of reversed segment
        prev.next.next = current
        prev.next = next_node  # prev.next to point to the new head of the reversed segment
        return dummy.next