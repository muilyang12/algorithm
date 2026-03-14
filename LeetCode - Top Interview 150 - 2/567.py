# Time Complexity: O(m)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_counts = {}
        for char in s1:
            if char not in s1_char_counts:
                s1_char_counts[char] = 0

            s1_char_counts[char] += 1

        left = 0
        right = left
        current_char_counts = {k: v for k, v in s1_char_counts.items()}

        while right < len(s2):
            if s2[right] not in current_char_counts:
                if s2[left] not in current_char_counts:
                    current_char_counts[s2[left]] = 0

                current_char_counts[s2[left]] += 1
                left += 1

            else:
                current_char_counts[s2[right]] -= 1
                if current_char_counts[s2[right]] == 0:
                    del current_char_counts[s2[right]]

                right += 1

            if len(current_char_counts) == 0:
                return True

        return False


"""
s1 = "abc", s2 = "eidbaocoo"
{a:1,b:1,c:1}

s1 = "adc", s2 = "dcda"
                   ! @
{a:1}
"""

"""
There is always a tricky part in Sliding Window. It's perfectly fine when left and right start at the same position with zero width, but it gets really difficult when the window is supposed to have a fixed width
from the start. I struggled with deciding when to update the values (adding right, removing left) versus when to move the pointers within the while loop. If I update before moving, it often conflicts with the initial
values set before the loop. If I update after moving, it leads to index errors in the final cycle.

When I discussed this with Gemini, it suggested not to start with left and right already spread apart, even for fixed-size windows. By carefully designing the conditions for moving right and left, and ensuring
the initial state is naturally handled by the right movement logic, the implementation becomes much simpler. That makes perfect sense. In Sliding Window problems, I should always initialize left and right to the
same position.
"""


# Time Complexity: O(nm)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_counts = {}
        for char in s1:
            if char not in s1_char_counts:
                s1_char_counts[char] = 0

            s1_char_counts[char] += 1

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            current_char_counts = {k: v for k, v in s1_char_counts.items()}
            for i in range(left, right + 1):
                if s2[i] not in current_char_counts:
                    break

                current_char_counts[s2[i]] -= 1

                if current_char_counts[s2[i]] == 0:
                    del current_char_counts[s2[i]]

            if len(current_char_counts) == 0:
                return True
            else:
                left += 1
                right += 1

        return False


"""
이 문제를 처음 봤을 때 나는 그렇게 생각했아. s1의 문자와 개수로 map을 만들고 s2에서 index를 찾아서 개수가 일치하는지를 체크한다. 그렇게 로직을 짰어. 이거를 left, right를 사용한 형식으로 바꿔서 한 번 더 작성을 했는데 변수명과 for-loop의 형태만 다르지 사실 상 같은 거야. 시간 복잡도도 O(nm) 아지.

sliding window 라는 알고리즘 유형의 본질은 들어오는 놈과 나가는 놈만 보자는 거잖아. 여기서도 마찬가지야. left와 right가 같이 넘어가면 right에 해당하는 놈을 고려하고 left - 1 에 대한 것만 고려하면 되는 거야. 알고리즘의 본질을 보려고 하자.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_counts = {}
        for char in s1:
            if char not in s1_char_counts:
                s1_char_counts[char] = 0

            s1_char_counts[char] += 1

        for i in range(len(s2) - len(s1) + 1):
            target_str = s2[i : i + len(s1)]

            temp_char_couts = {k: v for k, v in s1_char_counts.items()}
            for char in target_str:
                if char not in temp_char_couts:
                    break

                temp_char_couts[char] -= 1
                if temp_char_couts[char] == 0:
                    del temp_char_couts[char]

            if len(temp_char_couts) == 0:
                return True

        return False

