# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        # create dummy node
        # while both lists are not null, start with head of list 1
        # append if value less than head of list 2
        # keep comparing and appending until complete

        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next

        # edge case: if we finish with 4, and 5 leftover from example 1
        node.next = list1 or list2
            
        return dummy.next

        
        