# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev, curr, temp (next) pointers 
        # prev should be null
        # set curr next to prev
        # then curr becomes next
        # move next to the one after

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr # move to next
            curr = temp # move to next
        return prev 
        