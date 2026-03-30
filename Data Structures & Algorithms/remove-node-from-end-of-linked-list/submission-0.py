# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        total = 0

        dummy = head

        while dummy:
            total += 1
            dummy = dummy.next

        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        count, nodeToDelete = 1, total - n + 1


        while prev.next:
            if count == nodeToDelete:
                prev.next = prev.next.next
                break

            count += 1
            prev = prev.next

        return dummyHead.next
