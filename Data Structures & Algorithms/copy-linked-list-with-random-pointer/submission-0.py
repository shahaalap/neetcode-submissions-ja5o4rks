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

            pairs[(cur.val, cur.next, cur.random)] = curcopy

            cur = cur.next

        cur = head
        while cur is not None:
            curcopy = pairs[(cur.val, cur.next, cur.random)]
            if cur.random:
                curcopy.random = pairs[(cur.random.val, cur.random.next, cur.random.random)]

            cur = cur.next

        return dummyHead.next

