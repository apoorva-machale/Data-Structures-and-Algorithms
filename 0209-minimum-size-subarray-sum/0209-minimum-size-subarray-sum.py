class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start =0
        min_length = float('inf')
        total = 0
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                min_length = min(min_length, end-start+1)
                total -= nums[start]
                start+=1
        
        if min_length == float('inf'):
            return 0
        
        return min_length