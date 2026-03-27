class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = {}
        for char in s:
            if char not in char_counts:
                char_counts[char] = 0

            char_counts[char] += 1

        heap = []
        for char, count in char_counts.items():
            heapq.heappush(heap, (-count, char))

        result = ""
        cooldown = None

        while heap:
            count, char = heapq.heappop(heap)
            count = -count

            result += char
            count -= 1

            if cooldown:
                cooldown_char, cooldown_count = cooldown
                cooldown = None

                heapq.heappush(heap, (-cooldown_count, cooldown_char))

            if count > 0:
                cooldown = (char, count)

        return result if len(s) == len(result) else ""


"""
Heap-based problems always seem to share some common ground at the conceptual level.

First, there is the principle that you should use the elements with larger values first. Second, you must ensure that only the items currently available for use
are kept in the Heap.
"""
