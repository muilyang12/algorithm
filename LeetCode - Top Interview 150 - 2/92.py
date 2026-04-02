"""
To perform a reverse operation on a Linked List
1. Try to use only two pointers.
2. Use temporary variable since you must move the pointers only after changing the direction of the link.

While some cases start the previous pointer at `None` and others start it at a `dummy` node, that part is something you need to consider carefully based on the specific requirements.
"""


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right or not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        before_targets = dummy
        for _ in range(left - 1):
            before_targets = before_targets.next

        start_targets = before_targets.next

        previous = start_targets
        current = start_targets.next

        for i in range(right - left):
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        end_targets = previous
        after_targets = current

        before_targets.next = end_targets
        start_targets.next = after_targets

        return dummy.next


"""
 [1,2,3,4,5]
        p c

for _ in range(left - 1):

before_targets = p
start_range = c

for _ in range(right - left):

after_targets = n

before_targets.next = c
start_range.next = n
"""
