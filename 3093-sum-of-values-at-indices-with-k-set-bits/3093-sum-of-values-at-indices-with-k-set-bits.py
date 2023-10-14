class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            temp=i
            count=0
            flag=0
            while i>0:
                count+=i&1
                i=i>>1
                if count>k:
                    flag=1
                    break
            if count==k and not flag:
                res+=nums[temp]
        return res

            
        