# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return l1

        if l2 is None:
            l2 = ListNode()

        v = l1.val + l2.val

        l1.val = v % 10
        if v // 10 == 1:
            if l1.next is not None:
                l1.next.val += 1
            else:
                l1.next = ListNode(val=1)

        if l1.next is None and l2.next is not None:
            l1.next = ListNode()

        l1.next = self.addTwoNumbers(l1.next, l2.next)

        return l1