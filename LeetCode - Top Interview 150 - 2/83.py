class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = slow.next

        while fast:
            if slow.val == fast.val:
                slow.next = fast.next

                fast.next = None

                fast = slow.next
            else:
                slow = fast
                fast = slow.next

        return head
