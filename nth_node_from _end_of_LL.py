class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def getKthFromLast(self, head, k):
        # Step 1: Use two pointers
        first = head
        second = head

        # Step 2: Move 'first' k steps ahead
        for _ in range(k):
            if first is None:
                return -1  # k is larger than the length of the list
            first = first.next

        # Step 3: Move both pointers until 'first' reaches the end
        while first:
            first = first.next
            second = second.next

        # Step 4: 'second' now points to the k-th node from the end
        return second.data if second else -1