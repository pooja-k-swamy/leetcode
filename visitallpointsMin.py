class Solution:
    def countTime(self,X1,X2):
        x = abs(X1[1]-X2[1])
        y = abs(X1[0]-X2[0])
        return max(x,y)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for k in range(len(points)-1):
            count += self.countTime(points[k],points[k+1])
        return count