# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        
        if list2 and not list1:
            return list2

        x , y = list1, list2

        while x and y:

            while x.next and x.next.val <= y.val:
                x = x.next

            while y.next and y.next.val < x.val:
                y = y.next

            if x.val <= y.val:
                temp = x.next
                x.next = y
                x = temp
            else:
                temp = y.next
                y.next = x
                y = temp

        
        if list1 and list2 and list1.val <= list2.val:
            return list1
        else:
            return list2