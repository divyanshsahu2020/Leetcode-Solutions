class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        win_sum=0
        l=0
        r=0
        res=float('inf')
        while r<len(nums):
            while win_sum+nums[r]>=target:
                res=min(res,r-l+1)
                win_sum-=nums[l]
                l+=1
            win_sum+=nums[r]
            r+=1
        if(res==float('inf')):
            return 0
        return res
        

            