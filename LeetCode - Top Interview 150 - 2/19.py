class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        before_slow = dummy
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            before_slow = slow
            slow = slow.next
            fast = fast.next

        before_slow.next = slow.next
        slow.next = None

        return dummy.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next

        dummy = ListNode(-1)
        dummy.next = head
        before_target = dummy
        target = head

        while fast:
            fast = fast.next
            target = target.next
            before_target = before_target.next

        before_target.next = target.next
        target.next = None

        return dummy.next


"""
head = [1,2,3,4,5], n = 2
            # @   !
"""
