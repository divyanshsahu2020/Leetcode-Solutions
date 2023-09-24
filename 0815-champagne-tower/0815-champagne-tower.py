class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row=[poured]
        for i in range(1,query_row+1):
            curr_row=[0]*(i+1)
            for val in range(0,i):
                extra=prev_row[val]-1
                if(extra>0):
                    curr_row[val]+=extra/2
                    curr_row[val+1]+=extra/2
            prev_row=curr_row
        return min(1,prev_row[query_glass])
        