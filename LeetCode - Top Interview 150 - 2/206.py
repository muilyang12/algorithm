class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            first = head
            second = head.next

            second.next = first
            first.next = None

            return second

        first = head
        second = head.next
        third = head.next.next

        while third:
            second.next = first

            first = second
            second = third
            third = third.next

        second.next = first

        head.next = None

        return second


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first = None
        second = head
        third = head.next

        while third:
            second.next = first

            first = second
            second = third
            third = third.next

        second.next = first

        return second


"""
  [1,2,3,4,5]
 f s t
   f s t
     f s t
       f s t

Edge Case
  [1,2]
 f s t 
[1]
"""

"""
I think the idea of setting first to None and second to head is absolutely brilliant. I honestly don't know if I'll be able to recall such a clever trick next time.
"""
