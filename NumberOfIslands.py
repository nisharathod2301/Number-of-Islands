class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(sr, sc, start):
            
            if sr < 0 or sr >= rows or sc <0 or sc >= cols: return
            if grid[sr][sc] != start: return
            
            grid[sr][sc] = 2
            
            dfs(sr+1, sc, start)
            dfs(sr-1, sc, start)
            dfs(sr, sc+1, start)
            dfs(sr, sc-1, start)
       
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == "1":
                    islands += 1
                    prev = grid[r][c]
                    dfs(r, c, prev)
                    
        return islands
