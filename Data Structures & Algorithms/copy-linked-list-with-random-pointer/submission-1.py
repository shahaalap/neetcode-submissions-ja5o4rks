"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pairs = {}

        cur = head
        dummyHead = Node(0)
        prev = dummyHead

        while cur is not None:
            curcopy = Node(cur.val)
            prev.next = curcopy
            prev = prev.next

            pairs[cur] = curcopy

            cur = cur.next

        cur = head
        while cur is not None:
            curcopy = pairs[cur]
            if cur.random:
                curcopy.random = pairs[cur.random]

            cur = cur.next

        return dummyHead.next

