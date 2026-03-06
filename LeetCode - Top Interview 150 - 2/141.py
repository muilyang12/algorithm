class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


"""
There is an algorithm called Floyd's Cycle-Finding Algorithm, which is used to detect cycles in a Linked List. It uses two pointers, slow and fast, and concludes that a cycle exists when they meet. Let's keep this in mind.
"""

"""
I solved this problem twice because I struggled with how to set the condition for the while loop. Look, the fast pointer will always reach the end of the Linked List before the slow pointer. Therefore, you should use fast and fast.next as the conditions for the while loop.
"""
