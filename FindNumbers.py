'''
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if (math.floor(math.log10(nums[i])) == 1):
                count += 1
            elif (math.floor(math.log10(nums[i])) == 3):
                count += 1
            elif (math.floor(math.log10(nums[i])) == 5):
                count += 1
            else:
                continue
        return count
 '''   
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if ((math.floor(math.log10(nums[i])) == 1) | (math.floor(math.log10(nums[i])) == 3) | (math.floor(math.log10(nums[i])) == 5)):
                count = count + 1
            else:
                continue
        return count
