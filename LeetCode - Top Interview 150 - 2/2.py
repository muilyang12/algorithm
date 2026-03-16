class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        l1_current = l1
        l2_current = l2

        carry = 0

        while l1_current or l2_current:
            val1 = l1_current.val if l1_current else 0
            val2 = l2_current.val if l2_current else 0

            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10

            current.next = ListNode(val)
            current = current.next

            if l1_current:
                l1_current = l1_current.next
            if l2_current:
                l2_current = l2_current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_l1 = l1
        current_l2 = l2

        dummy = ListNode(-1)
        current = dummy

        carry = 0
        while current_l1 or current_l2:
            value = 0
            if current_l1 and current_l2:
                value = (current_l1.val + current_l2.val + carry) % 10
                carry = (current_l1.val + current_l2.val + carry) // 10
            elif current_l1 or current_l2:
                value = (
                    (current_l1.val + carry) % 10
                    if current_l1
                    else (current_l2.val + carry) % 10
                )
                carry = (
                    (current_l1.val + carry) // 10
                    if current_l1
                    else (current_l2.val + carry) // 10
                )

            if current_l1:
                current_l1 = current_l1.next
            if current_l2:
                current_l2 = current_l2.next

            current.next = ListNode(value)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


"""
To be honest, I thought the core idea for solving this problem was quite obvious since I've done it so many times. However, there was a trap. I made a mistake in the order of calculating the `carry`
and the `value`. Since the carry is a "bigger" concept, I instinctively wanted to calculate it first. But the value calculation actually depends on the current carry.  That's why I had to calculate
the carry later.
"""
