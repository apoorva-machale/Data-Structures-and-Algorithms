class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        for row in grid:
            start = 0
            end = n-1
            while start <= end:
                mid = (start + end) // 2
                if row[mid] < 0:
                    end = mid-1
                else:
                    start = mid+1
            count += (n-start)
        return count