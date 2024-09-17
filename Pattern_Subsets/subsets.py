def find_subsets(nums):
    subsets = []
    #start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        #we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            #create a new subset from the existing subset and insert the current element to it
            set = list(subsets[i])
            # print("1 ",set)
            set.append(currentNumber)
            # print("2 ", set)
            subsets.append(set)
            # print("subsets ",subsets)
            
    return subsets

result = find_subsets([1,5,3])
print(result)