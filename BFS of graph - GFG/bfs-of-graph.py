#User function Template for python3

from typing import List

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
    
        q=[]
        visited=set()
        res=[]
        q.append(0)
        while q:
            ele=q.pop(0)
            if ele in visited:
                continue
            if ele>=len(adj):
                continue
            visited.add(ele)
            res.append(ele)
            for neighbor in adj[ele]:
                q.append(neighbor)
        return res
                
        


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends