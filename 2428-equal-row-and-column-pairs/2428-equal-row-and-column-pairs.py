
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        col=[]
        for i in range(cols):
            temp=[]
            for j in range(rows):
                temp.append(grid[j][i])
            col.append(temp)
        count=0
        print(col)
        for i in col:
            count+=grid.count(i)
        return count
    


        
        