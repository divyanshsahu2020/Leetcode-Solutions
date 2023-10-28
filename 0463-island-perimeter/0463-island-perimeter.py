class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        def dfs(i,j):
            if(i,j) in visited:
                return 0
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]==0:
                return 1
            visited.add((i,j))
            res=0
            res+=dfs(i+1,j)
            res+=dfs(i-1,j)
            res+=dfs(i,j+1)
            res+=dfs(i,j-1)
            return res
        fres=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fres+=dfs(i,j)
        return fres
            
            


        