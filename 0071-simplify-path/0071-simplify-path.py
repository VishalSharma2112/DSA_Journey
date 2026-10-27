class Solution:
    def simplifyPath(self, path: str) -> str:
        left = 0
        arr = []
        for right in range(1, len(path)):
            if path[right]=='/':
                if right-left==1 and path[right] == '/' and path[left] == '/':
                    left = right
                    continue
                arr.append(path[left+1:right])
                left = right
        arr.append(path[left+1:])
        if path[len(path)-1] == '/':
            arr.pop()

        stack = ['/']
        for i in arr:
            if i=='..':
                if(len(stack)==1):
                    continue
                stack.pop()
            elif i=='.':
                continue
            else:
                stack.append(i)
        print(stack)

        ans = '/'.join(stack)
        print(ans)
        return ans if len(ans)==1 else ans[1:]

            


        return(arr)