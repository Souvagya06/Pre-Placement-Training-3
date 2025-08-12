class Solution:
    def insertInMiddle(self, head, x):
        # Step 1: Create the new node
        new_node = Node(x)

        # Step 2: Handle edge case: empty list
        if head is None:
            return new_node

        # Step 3: Use slow and fast pointers to find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 4: Insert the new node after 'slow'
        new_node.next = slow.next
        slow.next = new_node

        # Step 5: Return the head of the updated list
        return head