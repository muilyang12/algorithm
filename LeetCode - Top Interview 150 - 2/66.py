class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = deque()

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            new_value = digits[i] + carry

            if new_value >= 10:
                result.appendleft(new_value % 10)
                carry = 1
            else:
                result.appendleft(new_value % 10)
                carry = 0
        
        if carry == 1:
            result.appendleft(1)

        return list(result)


"""
[1,2,9,9]
       ^

carry = 1
for i in range(len(digits) - 1, -1, -1):
    new_value = i + carry

    if i + carry >= 10:
        result.leftappend(new_value % 10)
        carry = 1
    else:
        result.leftappend(new_value % 10)
        carry = 0
"""
