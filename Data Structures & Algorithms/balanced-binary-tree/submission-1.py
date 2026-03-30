# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root, 0)
        return self.balanced

    def height(self, root: Optional[TreeNode], h) -> int:
        if root is None:
            return h
        else:
            l = self.height(root.left, h + 1)
            r = self.height(root.right, h + 1)

            if l != r and l + 1 != r and r + 1 != l:
                self.balanced = False

            return max(l, r)