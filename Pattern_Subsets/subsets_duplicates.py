def find_duplicates(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets

result = find_duplicates([1, 3, 3, 5])
print(result)
             