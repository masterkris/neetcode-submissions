# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            first = q1.pop()
            second = q2.pop()

            if not first and not second:
                continue

            if first is None or second is None or first.val != second.val:
                return False
            
          
            q1.append(first.left)
            q2.append(second.left)
            q1.append(first.right)
            q2.append(second.right)
        
        return True
        


        
        