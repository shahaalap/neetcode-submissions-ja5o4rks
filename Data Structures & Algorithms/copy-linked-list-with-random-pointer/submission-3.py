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
        if head is None:
            return None
            
        #Copy
        cur = head
        while cur is not None:
            curCopy = Node(cur.val, cur.next)
            cur.next = curCopy

            cur = curCopy.next

        newHead = head.next
        #Update random
        cur = head
        while cur is not None:
            if cur.random:
                cur.next.random = cur.random.next
            
            cur = cur.next.next

        #Remove next links
        cur = head
        while cur is not None:
            curCopy = cur.next
            cur.next = cur.next.next

            if curCopy.next:
                curCopy.next = curCopy.next.next

            cur = cur.next

        return newHead
