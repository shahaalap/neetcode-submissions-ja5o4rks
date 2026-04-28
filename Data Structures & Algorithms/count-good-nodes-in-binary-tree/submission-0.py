# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        
        def helper(node, maxsofar):
            nonlocal result
            if node.val >= maxsofar:
                result += 1

            if node.left:
                helper(node.left, max(maxsofar, node.val))
            
            if node.right:
                helper(node.right, max(maxsofar, node.val))

        helper(root, -101)
        return result