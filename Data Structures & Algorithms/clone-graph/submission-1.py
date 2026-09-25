"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # given int. val and neighbors
        # deep copy -> brand new copy

        # edge case -> doesn't exist, return None
        # hashmap + queue approach
        # hashmap -> key to value mapping. Node to value mapping.
        # initialize hashmap with node, append to queue
        # while q, pop from queue. make sure we haven't seen neighbors, then make a deep copy of neighbors.
        # append to queue
        # return the deep copy

        if not node:
            return None

        cloned = {}
        q = deque()

        cloned[node] = Node(node.val)
        q.append(node)

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in cloned: # we haven't seen yet, add to hashmap
                    cloned[n] = Node(n.val)
                    q.append(n)
                cloned[curr].neighbors.append(cloned[n]) # adjacency list with neighbors
        
        return cloned[node]




        