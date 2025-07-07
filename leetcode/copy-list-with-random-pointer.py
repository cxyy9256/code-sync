"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
        # Step 1: Interleave original and copied nodes
        # Original:  A -> B -> C
        # Becomes:   A -> A' -> B -> B' -> C -> C'
        
        curr = head
        while curr:
            # insert a copy
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            
        # A.random = C, random is just a next that goes anywhere
        # assign random pointers to the copied nodes
        # Set the random pointers for the copied nodes
        # A'.random = A.random.next
        # B'.random = B.random.next
        
        curr = head
        while curr:
            if curr.random:
                # curr.next is the A'
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the interleaved list into original and copied
        curr = head
        copy_head = head.next
        
        while curr:
            copy = curr.next
            curr.next = copy.next # reassign curr.next to jump over the copy, # restore original node's next
            
            # need ot check because But at the end of the list, copy.next will be None (when you're at the last node C'). In that case, copy.next.next would throw an error 
            if copy.next:
                copy.next  = copy.next.next
            curr = curr.next
            
        return copy_head