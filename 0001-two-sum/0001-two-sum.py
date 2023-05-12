class Solution(object):
    def twoSum(self, nums, target):
        """
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums=nums
        self.target=target
        arr=[]
        print("hello")
        for count in range(0,len(nums)):
            diff=target-nums[count]
            if(diff in nums[count+1:]):
                arr.append(count)
                arr.append(nums.index(diff,count+1))
        return arr

                