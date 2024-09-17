from collections import deque

def find_permutations(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentnumber in nums:
        n = len(permutations)
        for _ in range(n):
            oldpermutation = permutations.popleft()
            for j in range(len(oldpermutation)+1):
                newpermutation = list(oldpermutation)
                newpermutation.insert(j,currentnumber)
                if(len(newpermutation) == numsLength):
                    result.append(newpermutation)
                else:
                    permutations.append(newpermutation)
    return result

result = find_permutations([1,3,5])
print(result)
                
            