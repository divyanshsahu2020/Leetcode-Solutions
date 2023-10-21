class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(nums)-1,-1,-1):
            while heap:
                ele=heap[0]
                if ele[1]-i<=k:
                    nums[i]=max(nums[i],nums[i]+(-ele[0]))
                    break
                else:
                    heapq.heappop(heap)
            heapq.heappush(heap,(-nums[i],i))

        return max(nums)



