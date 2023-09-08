class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=nums[::]
        temp=[]
        for i in range(len(nums)-1,-1,-1):
            temp=float('inf')
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i] and nums[j]<temp):
                    temp=nums[j]
            if temp!=float('inf'):
                arr=nums[i:]
                arr.remove(temp)
                nums[i]=temp
                arr.sort()
                for k in range(i+1,len(nums)):
                    nums[k]=arr.pop(0)
                break
        if(res==nums):
            nums.reverse()



