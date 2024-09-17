from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
    
    # a. Initialize the graph
    # count of incoming edges
    inDegree = {i:0 for i in range(vertices)} #print(inDegree)   {0: 0, 1: 0, 2: 0, 3: 0}
    #adjacency list graph
    graph = {i: [] for i in range(vertices)} # print(graph) {0: [], 1: [], 2: [], 3: []}
    
    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1 # increment child's inDegree
    
    # c. Find all sources ie. all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    
    # d. For each source, add it to the sortedOrder and subtract one from all of it's child
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]: #get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
                
    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []
    return sortedOrder

result = topological_sort(4, [[3, 2], [3,0], [2, 0], [2, 1]])
print(result)