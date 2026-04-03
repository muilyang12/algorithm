"""
To perform a reverse operation on a Linked List,
1. Use only two pointers
2. Since using two pointers requires a temporary variable, you must move the pointers after changing the direction of the link.
3. The starting point of the previous pointer can be either None or a dummy node. Consider the context and decide accordingly.
"""

"""
This problem is quite difficult. While the idea of reversing based on a specific range or count,  similar to the "92. Reverse Linked List II", is relatively intuitive, the fact that before and after
must exist outside the segment being reversed makes it hard to handle the final cycle when exactly k nodes remain. You should be able to identify this as a potential issue and propose it as an edge
case during the dry run process.
"""


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        before = dummy
        after = head

        while after:
            for _ in range(k):
                if not after:
                    return dummy.next

                after = after.next

            start, end = self.reverse_part(before.next, k)

            before.next = start
            end.next = after

            before = end

        return dummy.next

    # Returns start, end
    def reverse_part(self, from_node, count):
        if count == 1:
            return (from_node, from_node)

        previous = from_node
        current = from_node.next

        start_targets = previous
        start_targets.next = None

        for i in range(count - 1):
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        end_targets = previous

        return (end_targets, start_targets)


"""
head = [1,2,3,4,5]
            ^ ^
"""