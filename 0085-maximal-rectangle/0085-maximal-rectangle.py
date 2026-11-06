class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def nextSmall(arr):
            stack = []
            NSE = [0]*len(arr)
            for i in range(len(arr)-1, -1, -1):
                while(len(stack)!=0 and arr[i] < arr[stack[-1]]):
                    stack.pop()
                if len(stack) == 0:
                    NSE[i] = len(arr)
                else:
                    NSE[i] = stack[-1]
                stack.append(i)
            return NSE


        def previousSmall(arr):
            stack = []
            PSE = [0]*len(arr)
            for i in range(len(arr)):
                while(len(stack)!=0 and arr[i] <= arr[stack[-1]]):
                    stack.pop()
                if len(stack) == 0:
                    PSE[i] = -1
                else:
                    PSE[i] = stack[-1]
                stack.append(i)
            return PSE


        def histogram(arr):
            NSE = nextSmall(arr)
            PSE = previousSmall(arr)
            areaSingle = -1
            for i in range(len(arr)):
                areaSingle = max(arr[i]*(NSE[i]-PSE[i]-1), areaSingle)
            return areaSingle

        arr = [0]*len(matrix[0])
        area = -1
        for index, i in enumerate(matrix):
            for j in range(len(i)):
                if int(i[j])==0:
                    arr[j] = 0
                else:
                    arr[j] = int(arr[j])+int(i[j])
            area = max(histogram(arr), area)
        return area