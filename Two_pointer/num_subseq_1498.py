def numSubseq(nums, target):
        nums.sort()

        res, mod = 0, (10**9 + 7)

        left, right = 0, len(nums) - 1
        while  left <= right:
            if (nums[left] + nums[right]) > target:
                right -= 1
            else:
                res += 1 << (right - left)
                left += 1
        return res % mod

result = numSubseq([3, 5, 6, 7], 9)
print(result)