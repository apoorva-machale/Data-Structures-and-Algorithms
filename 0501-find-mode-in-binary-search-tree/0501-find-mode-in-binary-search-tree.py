# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            counter[node.val] += 1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        max_freq = max(counter.values())
        
        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)
        
        return ans