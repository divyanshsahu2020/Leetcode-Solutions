class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        l=len(nums1)
        median=0.0
        if(l%2==0):
            median=float(nums1[l//2])+float(nums1[(l//2)-1])
            
            median=float(median/2)
        else:
            median=float(nums1[l//2])
            median="%.5f" % median
        return float(median)