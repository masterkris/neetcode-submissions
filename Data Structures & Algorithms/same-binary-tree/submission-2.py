# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # BFS, check level-by-level using queue

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            first = q1.popleft() # p
            second = q2.popleft() # q

            if first is None and second is None:
                continue # keep going
            
            if first is None or second is None or first.val != second.val:
                return False

            q1.append(first.left)
            q1.append(first.right)
            q2.append(second.left)
            q2.append(second.right)
        
        return True