class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                temp_result = ""
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == "[":
                        temp_result = "".join(stack[i + 1 :])
                        stack = stack[:i]
                        break

                    temp_result += stack[i]

                count_str = ""
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] not in "0123456789":
                        count_str = "".join(stack[i + 1 :])
                        stack = stack[: i + 1]
                        break

                    if i == 0:
                        count_str = "".join(stack)
                        stack = []

                for _ in range(int(count_str)):
                    stack.append(temp_result)

            else:
                stack.append(char)

        return "".join(stack)


"""
"3[2]" => "222"
"3[\[]"

Can k be 2 digit number?
Can I assume s will be a valid?
"""

"""
3[a2[c]]

Stack
["a" "[" "a" "2" "[" "c"]  "]"

["a" "[" "a" "2"] "c"

["a" "c" "c" "a" "c" "c" "a" "c" "c"] 

Edge Cases
"10[MY]"
"""

"""
I keep falling into the habit of just 'solving' the problem, coding it up and hitting the submit button. I shouldn't do that. After writing the algorithm, I need to demonstrate that I can think procedurally and logically by walking through the examples step-by-step.
"""