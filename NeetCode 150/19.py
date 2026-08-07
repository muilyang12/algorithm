class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        before = dummy
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            before = slow
            slow = slow.next
            fast = fast.next

        before.next = slow.next

        return dummy.next
