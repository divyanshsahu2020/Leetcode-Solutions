class Solution:
    def pathfind(graph,start,end,path=[]):
        path=path+[start]
        if(start==end):
            return [path]
        if(start not in graph):
            return []
        paths=[]
        for child in graph[start]:
            temp=Solution.pathfind(graph,child,end,path)
            for i in temp:
                paths.append(i)
        return paths

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l=len(graph)
        graph_dict={}
        for i in range(l):
            graph_dict[i]=graph[i]
            start=0
            end=len(graph_dict)-1
        f=Solution.pathfind(graph_dict,start,end)
        return(f)

        