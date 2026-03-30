# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        if root is None:
            return self.result
        
        def height(node: Optional[TreeNode]) -> int:

            lheight = 0
            rheight = 0

            if node.left:
                lheight  = 1 + height(node.left)
            
            if node.right:
                rheight  = 1 + height(node.right)

            h = max(lheight, rheight)

            self.result = max(self.result, lheight + rheight)
            return h     
        
        height(root)
        return self.result