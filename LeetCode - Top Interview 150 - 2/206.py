class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous

            previous = current
            current = temp

        return previous


"""
 [1,2,3,4,5]
          ^ ^
"""

"""
I used to use three pointers whenever I solved this problem. However, using three pointers requires longer exception handling at the initial stage compared to using two. Therefore, let's use a `temp`
variable inside the loop and keep only two main pointers. For this specific problem, the initial `previous` must start as `None` so that the next of the first node becomes `None` after the reverse
operation.

Key Elements to Remember
1. Use only two pointers
2. Since using two pointers requires a temporary variable, you must move the pointers after changing the direction of the link.
3. The starting point of the previous pointer can be either None or a dummy node. Consider the context and decide accordingly. (If I had designed the logic to use before and after for this problem as
well, creating a dummy node would have been a viable option.)
"""


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
