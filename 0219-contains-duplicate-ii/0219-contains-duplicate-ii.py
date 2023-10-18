class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            nums[i]=(nums[i],i)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i][0]==nums[i+1][0] and abs(nums[i][1]-nums[i+1][1])<=k:
                return True
        return False