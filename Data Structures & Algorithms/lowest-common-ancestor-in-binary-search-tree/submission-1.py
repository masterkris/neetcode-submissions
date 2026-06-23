# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val: # bst property
                curr = curr.right # example 2 if p is 7 and q is 9

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left # other side
            
            else:
                return curr

        