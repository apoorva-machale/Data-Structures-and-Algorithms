#   https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

def countPlatforms(arr, dep):
    #Sorting affects the index for the railways but we do not require them 
    arr.sort()
    dep.sort()


    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans




if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    print("Minimum number of Platforms required ", countPlatforms(arr, dep))