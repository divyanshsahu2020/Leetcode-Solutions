class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic=dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        for arr in dic.values():
            if len(arr)>1:
                for i in range(len(arr)-1):
                    if abs(arr[i]-arr[i+1])<=k:
                        return True

            else:
                continue
        return False