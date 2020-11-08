class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # use dp
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0
        memo = dict()
        memo[(0,0)] = grid[0][0]
        for col in range(1, width):
            memo[(0,col)] = memo[(0,col-1)] + grid[0][col]
        for row in range(1, height):
            memo[(row,0)] = memo[(row-1,0)] + grid[row][0]
        for row in range(1, height):
            for col in range(1, width):
                memo[(row, col)] = grid[row][col] + min(memo[(row-1, col)], memo[(row, col-1)])
        return memo[(height-1, width-1)]

