# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        '''
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev # new head of the reverse
        '''
        
    # recursive way
        if not head or not head.next:
            return head # Base case: if the list is empty or has only 1 node, it's already reversed.
        new_head = self.reverseList(head.next) # recurses all the way down till the end till it reaches base case
        
        head.next.next = head #  # 5.next = 4, reverses it 
        head.next = None # prevent loops/cycles: 5 → 4, but the 4 → 5  ← STILL EXISTS
        
        return new_head # return the new head to show the partial progresses