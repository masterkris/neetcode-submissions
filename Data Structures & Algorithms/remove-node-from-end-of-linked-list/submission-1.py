# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # [1,2,3,4]

        dummy = ListNode(0, head) # val = 0, next = head
        
        # 2 pointer approach
        l = dummy
        r = head 
        # when end and gap is n, we have l right before node we must remove

        while n > 0:
            r = r.next
            n -= 1   # so r will be at 2 if n = 2
        
        # [1,2,3,4]
      #  l   r
        
    # we want:
    # [1,2,3,4]
    #    l   r

        while r:
            r = r.next
            l = l.next # so we can connect l to r after done
        
        l.next = l.next.next
        return dummy.next


        

        