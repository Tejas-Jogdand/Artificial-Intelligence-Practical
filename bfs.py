# graph = {1:[2,3], 2:[4],3:[4,7],4:[5,6],5:[],6:[],7:[]}
graph = {1:[2,3],2:[4,5],3:[6,7],4:[8],5:[8],6:[8],7:[8],8:[]}

visited = []
queue = []

def bfs(visited, queue, root):
    visited.append(root)
    queue.append(root)
    while queue :
        m = queue.pop(0)
        for adjoint in graph[m]:
            if adjoint not in visited:
                visited.append(adjoint)
                queue.append(adjoint)
    print(visited)

print("bfs for given graph is:")
bfs(visited, queue, 1)