# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # slow, fast to find the middle of the linked list
        # reverse second half of list
        # merge two halves one by one
        # 1 -> 2 -> 3 -> 4 -> 5

        # [2, 4, 6, 8, 10]
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 6 is slow
        
        # start from the one after middle
        start = slow.next
        prev = slow.next = None

        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp # reversal part done
        
        # [2, 4, 6, 10, 8] prev = 10

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1 
            first = temp1 # move to "original" next
            second = temp2 # move to "original" next
        
        # [2,10,4,8,6] --> done
        



        