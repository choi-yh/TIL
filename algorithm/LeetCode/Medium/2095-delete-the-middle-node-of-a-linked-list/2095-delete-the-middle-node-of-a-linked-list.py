# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0  
        cur_node = head
        while cur_node != None:
            length += 1
            cur_node = cur_node.next

        if length == 1:
            return None
        
        middle_idx = length // 2

        cur_node = head
        idx_count = 0
        while cur_node.next != None:
            idx_count += 1
            if idx_count == middle_idx:
                cur_node.next = cur_node.next.next
                return head

            cur_node = cur_node.next

        return head