graph = {
    1:[2,3],
    2:[4,5],
    3:[6,7],
    4:[8],
    5:[8],
    6:[8],
    7:[8],
    8:[]
}

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        visited.add(root)
        print(root)
        for neg in root[root]:
            dfs(visited, neg, root)

dfs(visited, graph, 1)