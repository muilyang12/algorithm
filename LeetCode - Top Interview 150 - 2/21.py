# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ref1 = list1
        ref2 = list2

        dummy = ListNode(-1)
        current = dummy

        while ref1 or ref2:
            if ref1 and ref2:
                if ref1.val <= ref2.val:
                    current.next = ListNode(ref1.val)
                    current = current.next

                    ref1 = ref1.next
                else:
                    current.next = ListNode(ref2.val)
                    current = current.next

                    ref2 = ref2.next

            elif ref1:
                current.next = ListNode(ref1.val)
                current = current.next

                ref1 = ref1.next

            else:
                current.next = ListNode(ref2.val)
                current = current.next

                ref2 = ref2.next

        return dummy.next
