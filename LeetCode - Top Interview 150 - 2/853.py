# Time Complexity: O(n log n + n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_speed = sorted(position_speed)

        result = 0

        while position_speed:
            result += 1
            cur_pos, cur_sp = position_speed.pop()
            time = (target - cur_pos) / cur_sp

            while (
                position_speed
                and position_speed[-1][0] + position_speed[-1][1] * time >= target
            ):
                position_speed.pop()

        return result
