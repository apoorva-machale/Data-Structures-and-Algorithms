class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeros = 0, 0
        for n in range(len(nums)):
            zeros += nums[n] == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        
        return n - l + 1