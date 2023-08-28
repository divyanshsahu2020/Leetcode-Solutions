class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            temp=i
            temp=temp.removeprefix('-')
            if not(temp.isdigit()):
                if(i=='D'):
                    res.append(2*(res[-1]))
                elif(i=='C'):
                    res.pop()
                else:
                    if(len(res)>=2):
                        res.append(res[-1]+res[-2])
                    elif(len(res)>=1):
                        res.append(res[-1])
                    else:
                        continue
            else:
                res.append(int(i))
        res=[int(i) for i in res]
        return( sum(res))