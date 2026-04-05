class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        return nums[slow]


"""
               D                   D
               -----               -----     |         |        |
L              C
===============++++++++++
0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2
                    s                   f
^                                       ^

Distance `s` moves = L + D
Distance `f` moves = L + D + nC

2(L + D) = L + nC + D
L = nC - D

The key is that if the pointer f moves by nC - D, it will reach the start of the cycle. In other words, if there is another pointer starting from 0 at this point, both f and
that pointer will meet at the cycle's entrance at the exact same time after advancing by L or nC - D.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

"""
set()

{1, 3, 4, 2}

2

O(n)
O(n)

=====

[1,3,4,2,2]

 1 2 4 3 5
     6   7
     8   9
    10  11
    12

[3,1,3,4,2]
 1   4 2 3
     7 5 6
     108 9

 0 1 2 3 4 5 6 7 8 9
[2,5,9,6,9,3,8,9,7,1]
 1 4 2 6   5 7 9 8 3
   11  13  1214161510
   18  20  1921232217
   25  27  2628302924

1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14
1,3,5,7,9,11,13,15,17,19,21,23,25,27
"""

"""
Seeing the range $[1, n+1]$, I'm supposed to recognize this as an index-based problem and look for a cycle. This approach feels like it relies too much on a specific 'aha!' moment or a clever trick. Why is this so important? Why do companies frequently ask this type of question? :(
"""

"""
Let’s assume we've correctly identified the need to find a cycle. Even after detecting it using Floyd’s Cycle-Finding Algorithm, we aren't done yet. In this problem, we actually need to find the entry point of the cycle. If we simply stop the loop when slow == fast, we might be stuck somewhere in the middle of the cycle, not at the start of it.

There is another technique for this, but honestly, it feels a bit like pure memorization, so I’m worried if I’ll be able to recall it next time.

L: Distance from the start to the cycle entry.
C: Total length of the cycle.
X: Distance from the cycle entry to where slow and fast first meet.

Distance moved by `slow`: L + X
Distance moved by `fast`: L + X + nC

2(L + X) = L + X + nC
L = nC - X

This means the distance from the starting point to the cycle entry is equal to the remaining distance from the meeting point forward to the cycle entry.

So, to solve this, you can use this technique. At the moment slow == fast, reset slow to the start and move both pointers one step at a time. The point where they meet again will be the entry of the cycle.
"""