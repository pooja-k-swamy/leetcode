class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            if (nums[i + 1] > len(nums)):
                break
            val = nums[i + 1]
            mid_ans = [val] * freq
            ans.extend(mid_ans)
            ''' Difference bn append and extend methods
            append would've added the list mid_ans to the initial list, but as a single element, which is a list.
            In other words, it doesn't append each element of mid_ans individually,but instead it appends the entire object 
            itself. The extend method, actually adds the individual elements of second list, 
            as separate and unique elements of the resulting list.
            '''
        return ans
