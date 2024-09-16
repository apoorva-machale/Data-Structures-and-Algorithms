#Array and BinarySearch
from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self) -> None:
        self.key_time_map = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        #If the key does not exist in dictionary
        if not key in self.key_time_map:
            self.key_time_map[key] = []
        
        #store (timestamp, value) pair in key bucket
        self.key_time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        #If key does not exist in dictionary we will return empty string
        if not key in self.key_time_map:
            return ""
        
        if timestamp < self.key_time_map[key][0][0]:
            return ""
        
        left=0
        right = len(self.key_time_map[key])
        while left < right:
            mid = left + (right-left) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid+1
            else:
                right = mid
        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.key_time_map[key][right - 1][1]
    
time_map = TimeMap()
result = [-1]*6
result[0] = time_map.set("foo", "bar", 1)
result[1] = time_map.get("foo", 1)
result[2] = time_map.get("foo", 3)
result[3] = time_map.set("foo","bar2", 4)
result[4] = time_map.get("foo", 4)
result[5] = time_map.get("foo", 5)

print(result)