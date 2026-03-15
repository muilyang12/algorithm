class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        pointers = [l for l in lists]

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while len(heap) > 0:
            _, from_index, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            pointers[from_index] = pointers[from_index].next
            if pointers[from_index]:
                heapq.heappush(
                    heap, (pointers[from_index].val, from_index, pointers[from_index])
                )

        return dummy.next


"""
This problem is challenging yet impressive. It looks like it can be solved in two ways.

First, create a Min Heap with a size equal to `len(lists)`. After extracting the minimum value, you refill the heap by taking the next element from the same list the value came from. Since each heap
operation takes O(log k) and you do this for all N nodes, the total time complexity is O(N log k).

Second, repeatedly merge the lists in pairs. If there are four lists, you first merge 0 with 1 and 2 with 3. Then, you merge the two resulting lists to get the final result. This process requires a
total of log k merge steps, and since each step involves N comparisons, the time complexity is also O(N log k).
"""

"""
I tried using a Heap.

1. The logic `lists[i] = lists[i].next` actually worked. Since accessing an array by index works on the concept of references. This logic simply updates lists[i] to refer to the next node of the current
reference. So it should function perfectly fine.

2. However, it feels a bit uneasy because it modifies the original lists. After talking with Gemini, it suggested the logic `pointers = [i for i in lists]`. Since the number of pointers is unknown, this
approach uses a shallow copy to extract only the references. By using `pointers[from_index] = pointers[from_index].next`, you can handle the pointers without any issues or affecting the original list
structure.

3. I got an error when I wrote `heapq.heappush(heap, (node.val, node, index))`. This happens because when you put a tuple in a heap, it automatically starts comparing from the first element. You know this,
right? If `node.val`is the same, it tries to compare the next element, but the `node` cannot be compared, which triggers the error. When pushing multiple values into a heap like this, you must use the order
`(node.val, index, node)`.
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while len(heap) > 0:
            _, from_index, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(
                    heap, (node.next.val, from_index, node.next)
                )

        return dummy.next
