"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # two pass solution
        # first pass copies the node, and also creates hashmap to map original node to new node
        # second pass for connecting pointers

        oldToCopy = { None : None } # hashmap, add None : None mapping

        cur = head
        while cur:
            copy = Node(cur.val) # deep copy of node with val
            oldToCopy[cur] = copy # map to new
            cur = cur.next
        
        # now actually connect the pointers
        cur = head
        while cur:
            copy = oldToCopy[cur] # get copy
            # set copy.next AND copy.random
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
        