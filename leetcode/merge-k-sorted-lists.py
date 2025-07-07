# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        while True:
            min_index = -1
            min_val = 1e9
            
            for i in range((len(lists))):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            
            # there is no more lists left
            if min_index == -1:
                break
            
            curr.next = lists[min_index]
            curr = curr.next
            
            lists[min_index] = lists[min_index].next
            
        return dummy.next