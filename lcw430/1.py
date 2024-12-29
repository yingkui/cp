from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        res = 0
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i-1][j]:
                    res += grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] = grid[i-1][j] + 1
        return res