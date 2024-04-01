class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums, target, key_part):
            keyIndex = -1
            start = 0
            end = len(nums) - 1
            while start<=end:
                mid = start + (end-start) // 2
                if nums[mid] < target:
                    start=mid+1
                elif nums[mid] > target:
                    end=mid-1
                else:
                    keyIndex = mid
                    if key_part:
                        start = mid+1
                    else:
                        end=mid-1
            return keyIndex
        
        result = [-1,-1]
        result[0] = binary(nums, target, False)
        if result[0] != -1:
            result[1] = binary(nums, target, True)
            return result
        return [-1, -1]
    
        