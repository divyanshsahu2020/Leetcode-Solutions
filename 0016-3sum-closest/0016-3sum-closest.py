class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        finalset=set
        closest=999999
        for i in range(len(nums)):
            differ=target-nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                diff=abs(target-s)
                if(diff<closest):
                    closest=diff
                    finalset=(nums[i],nums[l],nums[r])
                if(nums[l]+nums[r])>differ:
                    r=r-1
                else:
                    l=l+1
        return sum(finalset)
