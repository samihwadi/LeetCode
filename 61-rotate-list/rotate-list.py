# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If list is empty
        if not head:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # If k = length of list, list remains unchanged
        # Case 1
        # If list = [1, 2, 3], k = 4
        # list is rotated length + 1 time
        # Number of places moved = k % length
        # formula to find break (length - k - 1)
        # -1 since we are starting from head

        k = k % length
        if k == 0:
            return head
        break_at = length - k - 1
        curr = head
        for i in range(break_at):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head
        


        