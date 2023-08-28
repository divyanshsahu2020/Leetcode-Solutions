class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=0
        res=0
        total_sum=0
        while r<len(nums):
            total_sum+=nums[r]
            while nums[r]*(r-l+1)>total_sum+k:
                total_sum-=nums[l]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res

