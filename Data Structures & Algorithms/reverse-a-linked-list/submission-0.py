# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        def dfs(node: Optional[ListNode], parent: Optional[ListNode]):
            if node is None:
                self.resultNode = parent
                return
            
            dfs(node.next, node)
            parent.next = None
            node.next = parent

        dfs(head.next, head)
        return self.resultNode



