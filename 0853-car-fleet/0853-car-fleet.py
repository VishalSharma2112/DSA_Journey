class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = sorted(zip(position, speed))
        position = [p for p, s in pair]
        speed = [s for p, s in pair]
        print(position,speed)
        stack = []
        for i in range(len(position)-1, -1, -1):
            time = (target - position[i])/speed[i]
            if(len(stack) == 0):
                stack.append(time)
                continue
            if time<=stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
