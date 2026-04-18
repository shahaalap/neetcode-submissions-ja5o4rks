# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append((root,0))
        result = []

        while len(q):
            count = len(q)
            result.append([])

            while count > 0:
                node, level = q.popleft()
                result[level].append(node.val)

                if node.left:
                    q.append((node.left,level + 1))
                
                if node.right:
                    q.append((node.right, level + 1))

                count -= 1

        return result
