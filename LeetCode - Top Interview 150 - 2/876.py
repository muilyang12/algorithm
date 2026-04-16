class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


"""
1,2,3,4,5
!       !
@   @
1,2,3,4,5,6
!           !
@     @
"""
