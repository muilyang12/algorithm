"""
This problem is indeed excellent and highlights the importance of choosing between a for loop and a while loop. You can think of a `for` loop as a `while` loop where `current += 1`
is always called automatically.

In "75. Sort Colors," you shouldn't increment the current pointer when swapping with the right element because the newly brought-in value needed to be re-evaluated. This problem
also requires staying at the same index under certain conditions.

When a new asteroid survives a collision, the stack[-1] changes, but the logic to compare this surviving asteroid with the next potential target remains the same. While you could
write this identical logic inside both a for loop and a nested while loop, it is much smarter to use a single while loop. By not incrementing the current pointer when stack[-1] changes,
you can reuse the existing implementation to handle the newly updated stack[-1] without any extra code. Using a while loop combined with manual current pointer control is a very clever
way to keep the logic clean and efficient.
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        current = 0

        while current < len(asteroids):
            asteroid = asteroids[current]

            if not stack or stack[-1] < 0 or asteroid > 0:
                stack.append(asteroid)
                current += 1
            elif stack[-1] + asteroid == 0:
                stack.pop()
                current += 1
            elif abs(stack[-1]) > abs(asteroid):
                current += 1
            elif abs(stack[-1]) < abs(asteroid):
                stack.pop()

        return stack


"""
asteroids = [5,10,-5]

stack = [5, 10], -5

=====

asteroids = [10,2,-5]

Solved with stack.

previous 

stack = [10], -5

=====

asteroids = [10,2,-15]

stack = [], -15

=====

+ +
- +
- - 

+ -

=====

asteroids = [-2,-2,1,-2]

stack = [-2, -2, 1], -2
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or stack[-1] < 0 or asteroid > 0:
                stack.append(asteroid)

                continue

            last_popped = None
            while stack:
                if stack[-1] < 0 or asteroid > 0:
                    stack.append(asteroid)
                    last_popped = None
                    break
                elif stack[-1] + asteroid == 0:
                    last_popped = stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    last_popped = None
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    last_popped = stack.pop()

            if last_popped and abs(last_popped) < abs(asteroid):
                stack.append(asteroid)

        return stack
