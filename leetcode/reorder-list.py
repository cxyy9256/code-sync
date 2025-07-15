# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # slow and fast pointer technique to find midpoint
        '''
        Suppose the input is: 1 → 2 → 3 → 4 → 5, 
        find the midpoint as 3
        Split into: First half: 1 → 2 → 3 and Second half (to be reversed): 4 → 5

        Step 2: Reverse second half → 5 → 4

        Step 3: Merge:
        1 → 5 → 2 → 4 → 3
        '''
        if not head or not head.next:
            return 
        # step 1 to find the midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at the midpoint
        # step 2 is to reverse the second half
        # initially want the 4 in the example above to connect 
        prev, curr = None, slow.next
        slow.next = None # cutting into the first half 
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp # move on to the 5 to connect back to the 4

        # could just use prev too i think 
        second_half = prev 

        # step 3: merge the two halfs
        first = head
        while second_half:
            tmp1, tmp2 = first.next, second_half.next
            first.next = second_half
            second_half.next = tmp1
            first = tmp1
            second_half = tmp2