# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Easy solution
        # Think of it like two runners on a circular track
        # If one runner is faster, it will eventually lap the other
        # Tortoise & Hare (Floyd's Cycle Detection)
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False
