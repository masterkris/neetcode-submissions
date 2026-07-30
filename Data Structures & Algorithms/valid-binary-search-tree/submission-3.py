# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # smells like BFS
        # Plan:
        # edge case: if root null, return True
        # declare queue q
        # initialize with [root, left, right] val = [root, -inf, inf]
        # while queue, 
        # pop from queue
        # if node.val < left or > right at any point, return False
        # if left node exists, add to queue. same with right

        if not root:
            return None
        
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if node.val <= left or node.val >= right:
                return False
            
            if node.left:
                q.append((node.left, left, node.val))
            
            if node.right:
                q.append((node.right, node.val, right))
        
        return True


        