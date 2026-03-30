# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 1)])
        result = 0

        if not root:
            return result

        while len(queue) > 0:
            
            item = queue.pop()
            node = item[0]
            height = item[1]
            result = max(result, height)

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))

        return result