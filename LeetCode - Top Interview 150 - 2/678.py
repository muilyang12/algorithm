"""
`open_count_min`, `open_count_max` 이렇게 두 개의 변수를 사용한다는 아이디어. "*"를 만나게 되면 min, max가 2 칸씩 벌어지게 돼. 왜냐면 ")"인 경우에는 -1 일테고 ""인 경우에는 0일테고 ")"인 경우에는 +1 일테니까. 그리고 min이 음수가 되면 0으로 다시 세팅해준다. 왜냐면 음수가 된 경우에는 그냥 '아 아까 만났던 한 "*"가 ")"는 아니었겠구나' 이런 느낌으로 처리하는 거지. for loop 안에서 max가 음수로 내려가지면 그거는 "*"도 부족하고 ")"가 너무 많다는 의미이니 바로 False이야. 그리고 for loop 밖에서 min이 여전히 양수이면 그거는 "*"도 부족하고 "("가 너무 많다는 의미이니 False인거고.
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
