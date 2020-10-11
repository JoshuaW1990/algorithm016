class Solution(object):
    def updateBoard(self, board, click):
        """
        dfs
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        height = len(board)
        if height <= 0:
            return board
        width = len(board[0])
        if width <= 0:
            return board

        def countNeighborMine(row, col):
            result = 0
            for x in [row-1, row, row+1]:
                for y in [col-1, col, col+1]:
                    if x == row and y == col:
                        continue
                    if x < 0 or x >= height:
                        continue
                    if y < 0 or y >= width:
                        continue
                    if board[x][y] == 'M':
                        result += 1
            return result

        def dfs(row, col):
            if board[row][col] != 'E':
                return
            mine_num = countNeighborMine(row, col)
            if mine_num > 0:
                board[row][col] = str(mine_num)
                return
            board[row][col] = 'B'
            for x in [row-1, row, row+1]:
                for y in [col-1, col, col+1]:
                    if x < 0 or x >= height:
                        continue
                    if y < 0 or y >= width:
                        continue
                    if board[x][y] != 'E':
                        continue
                    dfs(x, y)

        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        dfs(row, col)
        return board


solution = Solution()
board = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
click = [0,0]
print(solution.updateBoard(board, click))