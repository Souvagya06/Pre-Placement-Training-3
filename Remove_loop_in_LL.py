class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head

        # Step 1: Detect loop using Floyd’s algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return  # No loop found

        # Step 2: Find the start of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Find the node just before the start of the loop
        while fast.next != slow:
            fast = fast.next

        # Step 4: Remove the loop
        fast.next = None