class node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    def deleteNode(self, head, k):
        # If the list is empty or k is invalid
        if head is None or k <= 0:
            return head

        # If the first node is to be deleted
        if k == 1:
            return head.next

        # Traverse to the (k-1)th node
        current = head
        for i in range(k - 2):
            if current is None or current.next is None:
                return head  # k is out of bounds
            current = current.next

        # Delete the k-th node
        if current.next:
            current.next = current.next.next

        return head