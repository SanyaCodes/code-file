"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # visit each spot once
        # easiest way to mark visited ones is by changing them to 0
        # if 1 is found, begin finding adjecent 1s
        # when found make it 0 to mark visited and add adjacent 1 coordinates to stack
        # keep emptying stack by solving each added 1 coordinate and when empty you have covered the entire island
        # go to next found 1 in the grid

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    stack = [(i,j)]
                    while stack:
                        x,y = stack.pop()
                        if x > 0 and grid[x-1][y] == '1':
                            grid[x-1][y] = '0'
                            stack.append((x-1,y))
                        if x+1 < m and grid[x+1][y] == '1':
                            grid[x+1][y] = '0'
                            stack.append((x+1,y))
                        if y > 0 and grid[x][y-1] == '1':
                            grid[x][y-1] = '0'
                            stack.append((x,y-1))
                        if y+1 < n and grid[x][y+1] == '1':
                            grid[x][y+1] = '0'
                            stack.append((x,y+1))
        return island

        
