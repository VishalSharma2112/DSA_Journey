class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if len(stack) != 0:
                temp = stack[-1]
                if i == "+":
                    stack.pop()
                    stack[-1] = stack[-1]+temp
                elif i == "-":
                    stack.pop()
                    stack[-1] = stack[-1]-temp
                elif i == "*":
                    stack.pop()
                    stack[-1] = stack[-1]*temp
                elif i == "/":
                    stack.pop()
                    stack[-1] = int(stack[-1]/temp)
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        return stack[0]
        