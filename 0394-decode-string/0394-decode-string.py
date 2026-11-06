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

                for i in range(num):
                    for j in range(len(stack2)-1, -1, -1):
                        stack.append(stack2[j])
            else:
                stack.append(s[i])
        return ''.join(stack)