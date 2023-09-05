class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                r=mid-1
            elif(nums[mid]==target):
                if(mid-1<0):
                    res.append(mid)
                    break
                elif(nums[mid-1]==target):
                    r=mid-1
                else:
                    res.append(mid)
                    break
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                r=mid-1
            elif(nums[mid]==target):
                if(mid+1==len(nums)):
                    res.append(mid)
                    break
                elif(nums[mid+1]==target):
                    l=mid+1
                else:
                    res.append(mid)
                    break
        if(res):
            return res
        return [-1,-1]

