#Given an undirected graph with weighted edge
#Find the path with maximum probability from a given start to end

def max_probability(n: int, edges: list[list[int]], 
                    succ_prob: list[float], start_node: int, 
                    end_node: int) -> float:
    max_prob = 0
    if start_node > end_node:
        start_node, end_node = end_node, start_node

    weights = dict()
    for i in range(0,len(edges)):
        weights[(edges[i][0],edges[i][1])] = succ_prob[i]

    graph = dict()
    for edge in edges:
        for i in range(0,2):
            if edge[i] not in graph:
                graph[edge[i]] = []
            graph[edge[i]].append(edge[(i+1)%2])

    
    def find_paths(curr_node: int, end_node: int, 
                  current_prob: float):
        nonlocal max_prob
        for leaf in graph[curr_node]:
            if leaf in seen:
                continue
            seen.add(leaf)
            current_prob *= weights[curr_node, leaf]
            if leaf == end_node:
                if max_prob < current_prob:
                    max_prob = current_prob
                    current_prob *= (1/weights[curr_node, leaf])
                    seen.remove(leaf)
                    continue
            find_paths(leaf, end_node, current_prob)
            current_prob *= (1/weights[curr_node, leaf])

    seen = set([start_node])
    find_paths(start_node, end_node, 1)

    return max_prob


print(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))