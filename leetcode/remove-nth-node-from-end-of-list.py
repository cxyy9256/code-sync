# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        # nth node from the endd
        # want the slow pointer to land just before the node to remove
        '''
        
        To do that:

        Move fast n + 1 steps ahead

        Then move both fast and slow one step at a time

        When fast hits the end, slow is just before the target node
        
         index of the nth node from the end is:  target = L - n
         
         we want slow to stop at: L - n - 1
         
         if we move fast n + 1 steps ahead of slow, then: fast is at index n + 1, slow is still at index 0 and when fast reaches L, then slow will reach L - n - 1
        
        len(list) - (len(list) - n) + 1 = n +1 how to get to the end 
        
        len(list) - n is how many skips needed to get right before the skip over  
        
        
    
        '''
        dummy = ListNode(0, head)
        
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
                
        return dummy.next