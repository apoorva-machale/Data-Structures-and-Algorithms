class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(nums[i] * nums[i])
        res.sort()
        return res