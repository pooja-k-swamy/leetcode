class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = []
        for i in range(m):
            P.append(i+1)
        ans = []
        for i in queries:
            x = P.index(i)
            #x = P[i]
            y = P[x]
            ans.append(x)
            P.remove(y)
            P.insert(0, y)
            #print(ans)
        return ans