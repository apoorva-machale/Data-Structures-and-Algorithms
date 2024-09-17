class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBinaryTree(parent, values):
    n = len(parent)
    nodes = [TreeNode(val) for val in values]
    
    for i in range(n):
        if parent[i] != -1:
            if not nodes[parent[i]].left:
                nodes[parent[i]].left = nodes[i]
            else:
                nodes[parent[i]].right = nodes[i]

    return nodes[0]

def findMaxSum(root):
    def dfs(node):
        nonlocal max_sum
        
        if not node:
            return 0

        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))

        max_single = max(left_sum, right_sum) + node.val
        max_path = max(max_single, left_sum + right_sum + node.val)
        
        max_sum = max(max_sum, max_path)
        
        return max_single

    max_sum = float('-inf')
    dfs(root)
    return max_sum

# Example usage:
parent = [-1, 0, 1, 2, 0]
values = [-2, 10, 10, -3, 10]

root = constructBinaryTree(parent, values)
result = findMaxSum(root)
print(result) # Output will be 28

