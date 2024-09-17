def pair_sum(arr, target):
    nums ={}
    for i, num in enumerate(arr):
        # print("condition",target - num)
        if target - num in nums:
            # print("if",[nums[target-num],i])
            return [nums[target-num],i]
        else:
            nums[arr[i]]=i
            # print("else",nums)
    return [-1,-1]

result = pair_sum([1,2,3,4,6], target = 6)
print(result)