# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        
        # create dummy listNode so we can always track head

        # prev = dummy
        # iterate until we find node before left

        # set curr to the left node (after prev)
        # then do standard reverse algo --> right - left times

        # return dummy.next

        # O(n) time, O(1) space

        dummy = ListNode(0)
        dummy.next = head

        # reach right node and store node RIGHT after
        prev2 = dummy
        for i in range(right):
            prev2 = prev2.next
        
        connect = prev2.next # 4 in example

        # reach node before left
        before = dummy
        for i in range(left - 1):
            before = before.next
        
        # store left node and start from here
        curr = before.next
        prev = connect

        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        before.next = prev

        return dummy.next
        

        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        


        