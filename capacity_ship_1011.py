def feasible(weights, c, days):
    daysNeeded = 1
    currentLoad = 0
    for weight in weights:
        currentLoad += weight
        if currentLoad > c:
            daysNeeded += 1
            currentLoad = weight
    return daysNeeded <= days

def shipwithindays(weights, days):
    totalLoad = 0
    maxLoad = 0
    for weight in weights:
        totalLoad += weight
        maxLoad = max(maxLoad, weight)
    
    l = maxLoad
    r = totalLoad
    while l < r:
        mid = l + (r-l)// 2
        if feasible(weights, mid, days):
            r = mid
        else:
            l = mid + 1
    return l


result = shipwithindays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(result)