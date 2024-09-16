def count_negative(grid):
    count=0
    n=len(grid[0])
    for row in grid:
        start = 0
        end=n-1
        # print("row", row)
        while start <= end:
            # print("start,end",start,end)
            mid = start+(end-start) // 2
            print(mid)
            if row[mid] >= 0:
                start = mid+1
            else:
                end=mid-1
            # print(start,end)
        # print("count",n,start, count)

        count += (n-start)
    return count


grid = [[3,2], [1,0]]
count = count_negative(grid)
print(count)