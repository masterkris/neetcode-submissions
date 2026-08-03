# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque()
        res = []
        counter = 0
        q.append(root)
        
        while q:
            level = deque()
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                if counter % 2 == 0:
                    level.append(node.val) # default is right
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
            res.append(list(level))
            counter += 1
        
        return res
            
        