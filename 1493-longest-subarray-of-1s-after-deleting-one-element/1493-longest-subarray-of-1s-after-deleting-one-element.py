class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        w_size = 0
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while(zeros>1):
                zeros -= (nums[start]==0)
                start+=1
            w_size = max(w_size,i-start)
        return w_size
        
        