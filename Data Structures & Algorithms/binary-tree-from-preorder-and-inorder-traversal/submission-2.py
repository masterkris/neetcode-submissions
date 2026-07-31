# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder = curr, left, right
        # inorder = left, curr, right

        # preorder[0] is root

        # [1, 2, 3, 4]
        # [2, 1, 3, 4]

        # the left subtree consists of 2, so preorder[1: mid + 1] or inorder[:mid]
        # right subtree consists of 3,4, so preorder[mid + 1: ] or inorder[mid + 1: ]

        # this works as a general algorithm for this question

        # return root
        # [0: mid] - includes 0, excludes mid
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid + 1], inorder[0: mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root





        