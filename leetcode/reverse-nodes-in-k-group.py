# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def get_kth_node(curr, k):
            # jump k away from starting point
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = get_kth_node(group_prev, k)
            # Because we must only reverse if we have exactly k nodes ahead.

            if not kth:
                break
                
            group_next = kth.next
            
            # reverse from group_prev.next (=1) up to (but not including) group_next (=3) (in first iterations)
            # kth.next is all the way on the other side
            # 
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next