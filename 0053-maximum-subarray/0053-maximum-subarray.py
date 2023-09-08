class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        res=min(nums)
        for i in nums:
            curr_sum+=i
            res=max(res,curr_sum)
            curr_sum=max(curr_sum,0)
        return res