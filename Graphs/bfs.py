from collections import defaultdict, deque

def bfs_example(city_nodes, city_from, city_to, company):
    graph = defaultdict(list)
    for f, t in zip(city_from, city_to):
        graph[f].append(t)
        graph[t].append(f)
    # deque - [(1, 0)] after adding company, 0
    queue = deque([(company, 0)])
    print(queue)
    # visited = {1} after adding company
    visited = set([company])
    print(visited)
    distances = defaultdict(list)
    while queue:
        city, dist = queue.popleft()
        distances[dist].append(city)
        # print(city, dist)
        for neighbor in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist+1))
    
    result = []
    for dist in sorted(distances.keys()):
        result.extend(sorted(distances[dist]))
    
    result.remove(company)
    return result

city_nodes = 4
city_from = [1, 2, 2]
city_to = [2, 3, 4]
company = 1
result = bfs_example(city_nodes, city_from, city_to, company)
print(result)
