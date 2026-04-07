"""
s = "(*))"
1 0 0 0
1 2 1 0

=====

open_count_min
open_count_max

"(" +1 +1
"*" -1 +1
")" -1 -1

min < 0 -> set 0
max < 0 -> return False

min == 0 -> return True
min != 0 -> return False
"""


"""
Core idea
1. Use two variables, `open_count_min` and `open_count_max`.
2. When you encounter a "*", the gap between these minimum and maximum counts widens by two because the asterisk can represent a ) which is -1, an empty string which is 0,
or a "(" which is +1.
3. If the `open_count_min count becomes negative, you should reset it to 0 because this adjustment simply means that a previous "*" must not have functioned as a closing
parenthesis in that case.
4. If the maximum count ever drops below zero during the for-loop, you must call `return False` immediately since this indicates that there are too many closing parentheses
even with the help of "*"s.
5. If the minimum count remains positive after the loop finishes, you should also call `return False` because it signifies that there were too many opening parentheses and
not enough asterisks to balance them out.
"""

"""
"(*)"
1 0 0
1 2 1

"(**("
1 0 0 1
1 2 3 4
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count_min = 0
        open_count_max = 0

        for char in s:
            if char == "(":
                open_count_min += 1
                open_count_max += 1
            elif char == ")":
                open_count_min -= 1
                open_count_max -= 1
            else:
                open_count_min -= 1
                open_count_max += 1

            if open_count_min < 0:
                open_count_min = 0

            if open_count_max < 0:
                return False

        if open_count_min == 0:
            return True
        else:
            return False
