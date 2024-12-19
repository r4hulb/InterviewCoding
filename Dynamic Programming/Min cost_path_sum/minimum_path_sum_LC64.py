# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0]) if m else 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    pass
                elif i == m-1:
                    grid[i][j] += grid[i][j+1]
                elif j == n-1:
                    grid[i][j] += grid[i+1][j]
                else:
                    #print(i,j)
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
