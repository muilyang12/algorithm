# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        double_end_queue = deque()

        current = head.next

        while current:
            next_node = current.next

            current.next = None
            double_end_queue.append(current)

            current = next_node

        current = head

        while len(double_end_queue) >= 2:
            current.next = double_end_queue.pop()
            current = current.next
            current.next = double_end_queue.popleft()
            current = current.next

        if double_end_queue:
            current.next = double_end_queue.pop()


"""
1, 2, 3, 4, 5, 6, 7, 8

1, 8, 2, 7, 3, 6, 4, 5
"""
