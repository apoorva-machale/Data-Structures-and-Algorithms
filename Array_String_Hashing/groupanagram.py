from collections import defaultdict

def groupanagram(strs: list):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
        # print(ans)
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupanagram(strs)
print(result)
