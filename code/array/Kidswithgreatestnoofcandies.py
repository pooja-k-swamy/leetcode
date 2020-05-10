class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        bool_output = [False] * len(candies)
        for i in range(len(candies)):
            if ((candies[i] + extraCandies) >= greatest):
                bool_output[i] = True
            else:
                pass
        return bool_output
