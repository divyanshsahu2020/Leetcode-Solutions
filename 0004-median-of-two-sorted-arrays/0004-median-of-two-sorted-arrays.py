class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if(n%2==0):
            first=n//2
            second=first-1
            x=(nums[first]+nums[second])/2
            return x
        else:
            first=n//2
            return nums[first]