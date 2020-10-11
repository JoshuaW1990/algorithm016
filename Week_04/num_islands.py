class Solution(object):
    def numIslands(self, grid):
        """
        dfs + count
        :type grid: List[List[str]]
        :rtype: int
        """
        height = len(grid)
        if height <= 0:
            return 0
        width = len(grid[0])
        if width <= 0:
            return 0

        def dfs(row, col):
            if row < 0 or row >= height:
                return
            if col < 0 or col >= width:
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        result = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    result += 1
                    dfs(row, col)
        return result