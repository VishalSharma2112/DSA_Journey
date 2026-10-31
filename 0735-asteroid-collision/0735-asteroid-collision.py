class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for i in asteroids:
            alive = True

            while stack and stack[-1] > 0 and i < 0 and alive:

                if abs(stack[-1]) < abs(i):
                    stack.pop()

                elif abs(stack[-1]) == abs(i):
                    stack.pop()
                    alive = False

                else:
                    alive = False

            if alive:
                stack.append(i)

        return stack