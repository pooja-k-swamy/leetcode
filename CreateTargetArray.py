class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, ind in zip(nums, index):
            target.insert(ind, num)
            print(target)
        return target