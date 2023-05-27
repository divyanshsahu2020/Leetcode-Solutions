class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        curr=[1]
        ans=[]
        ans.append(curr)
        
        sum=0
        temp=[]
        for i in range(numRows-1):
            summ_arr=[]
            l=len(curr)
            for j in range(l-1):
                sum=curr[j]+curr[j+1]
                summ_arr.append(sum)
            curr=[curr[0]]+summ_arr+[curr[-1]]
            ans.append(curr)
        return(ans)



        