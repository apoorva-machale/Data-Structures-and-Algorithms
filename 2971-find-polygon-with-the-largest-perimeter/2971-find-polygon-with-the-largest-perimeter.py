class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        total = nums[0]
        max_total = -1
        for i in range(1,len(nums)-1):
            total += nums[i]
            if total > nums[i+1]:
                max_total = max(total+nums[i+1],max_total)
        return max_total
        
        