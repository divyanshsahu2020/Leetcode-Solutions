class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        d = dict()
        stack=[]
        curr_len=0
        sorted_people = sorted(people)
        flowers.sort()
        for i in sorted_people:
            if i in d:
                continue
            while flowers and flowers[0][0]<=i:
                heapq.heappush(stack,flowers.pop(0)[1])
                curr_len+=1

            while stack and stack[0]<i:
                heapq.heappop(stack)
                curr_len-=1
            d[i]=curr_len
        res=[]
        for k in people:
            res.append(d[k])
        return res