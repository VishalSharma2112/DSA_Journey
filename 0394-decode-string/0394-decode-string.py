class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack)!=0 and s[i] == ']':
                stack2 = []
                while stack[-1] != '[':
                    stack2.append(stack[-1])
                    stack.pop()
                stack.pop()
                temp = ''
                while (len(stack)!=0 and stack[-1].isdigit()):
                    temp += stack[-1]
                    stack.pop()
                num = int(temp[::-1])

                stack.extend(stack2[::-1] * num)
            else:
                stack.append(s[i])
        return ''.join(stack)