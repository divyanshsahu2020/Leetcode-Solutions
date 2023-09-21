class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        def dfs(i,j):
            if(i,j) in visited:
                return 0
            if(i<0 or i==len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0):
                return 0
            visited.add((i,j))
            return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    res=max(res,dfs(i,j))
        return res


        