class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            if(n==(mid)*(mid+1)//2):
                return mid
            elif(n<(mid)*(mid+1)//2):
                r=mid-1
            else:
                l=mid+1
        return l-1