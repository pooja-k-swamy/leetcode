class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    cnt += 1
            ans.append(cnt)
        return ans