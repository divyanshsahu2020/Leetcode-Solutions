#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        graph=defaultdict()
        for i,j in enumerate(adj):
            graph[i]=j
        stack=[]
        stack.append(0)
        res=[]
        visited=set()
        while stack:
            ele=stack.pop()
            if(ele in visited):
                continue
            visited.add(ele)
            res.append(ele)
            for neighbor in graph[ele][::-1]:
                stack.append(neighbor)
        return res


    


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends