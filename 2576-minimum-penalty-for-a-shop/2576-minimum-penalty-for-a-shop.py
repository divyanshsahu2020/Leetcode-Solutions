class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr=[]
        res=float('inf')
        res_inde=float('inf')
        for i in customers:
            if(i=='Y'):
                arr.append(1)
            else:
                arr.append(0)
        prefix_sum=0
        tsum=sum(arr)
        for i in range(len(arr)+1):
            penalty=i-prefix_sum
            temp=tsum-prefix_sum+penalty
            if(temp<res):
                res=min(res,temp)
                res_inde=i
            if not(i==len(arr)):
                prefix_sum+=arr[i]
        return res_inde
