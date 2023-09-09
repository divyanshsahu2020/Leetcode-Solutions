class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def helper(arr,target,memo={}):
            if(target in memo):
                return memo[target]
            if(target==0):
                return 1
            if(target<0):
                return 0
            res=0
            for i in arr:
                remainder=target-i
                no_of_ways=helper(arr,remainder)
                res+=no_of_ways
            memo[target]= res
            return memo[target]
        return helper(nums,target)