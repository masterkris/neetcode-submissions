# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # left, curr, right

        res = []

        def inorder(curr):
            if not curr:
                return []
            
            inorder(curr.left)
            res.append(curr.val)
            inorder(curr.right)
        
        inorder(root)
        return res
        