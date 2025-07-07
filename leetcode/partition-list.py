# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head
        
        current = head
        while current:
            if current.val<x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        less.next = greater_head.next
        greater.next = None

        return less_head.next