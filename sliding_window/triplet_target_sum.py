# Find Triplet sum close to target

def triplet_target_sum(nums, target):
    start = 0 
    s_diff = float(int)
    for end in range(len(nums)):
        sum += nums[end]
        if end-start+1 == 3:
            diff = target - sum
            if abs(diff) < abs(s_diff):
                s_diff = diff
            
    return result

nums = [-2, 0, 1, 2]
nums.sort()
result = triplet_target_sum(nums, target = 2)
print("Result", result)