class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(numRows-1):
            curr=res[-1]
            temp=[curr[0]]
            for j in range(0,len(curr)-1):
                temp.append(curr[j]+curr[j+1])
            temp.append(1)
            res.append(temp)
        return res

