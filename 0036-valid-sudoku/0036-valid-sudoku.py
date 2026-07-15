class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = True
        maps = {}
        boxes = {}
        for i in range(1, 10):
            maps[i] = {}
        for i in range(1, 10):
            boxes[i] = {}
        for row, i in enumerate(board, start=1):
            row_check = [0]*9
            for column, j in enumerate(i, start=1):
                if j != ".":
                    num = int(j)
                    if row_check[num-1] == 0:
                        row_check[num-1] = 1
                    else:
                        return False
                    if num not in maps[column]:
                        maps[column][num] = row
                    else:
                        return False
                    box = ((row - 1) // 3) * 3 + ((column - 1) // 3) + 1

                    if num in boxes[box]:
                        return False
                    boxes[box][num] = (row, column)
        return True