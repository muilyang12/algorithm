class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        charArrs = [[] for _ in range(numRows)]

        current = 0
        is_moving_down = True
        for char in s:
            charArrs[current].append(char)
            if is_moving_down:
                current += 1
            else:
                current -= 1

            if current >= numRows:
                current = numRows - 2
                is_moving_down = False
            elif current < 0:
                current = 1
                is_moving_down = True

        result = ""
        for chars in charArrs:
            result += "".join(chars)

        return result


"""
PAYPALISHIRING

3

PAYPALISHIRING
!   !   !   !
 @ @ @ @ @ @ @
  #   #   #

P   A   H   N
A P L S I I G
Y   I   R

4

PAYPALISHIRING
!@#$#@!@#$#@!@  

P     I     N
A   L S   I G
Y A   H R
P     I

ABC, 1

A B C

=====

Edge

When empty string comes in ""
When rowNums is 1
"""
