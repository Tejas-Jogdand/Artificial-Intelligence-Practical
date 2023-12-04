# breadth first search

# 1->2,3 ; 2->4 ; 3->4,7 ; 4->5,6 . this is graph.

graph = {1:[2,3],
         2:[4],
         3:[4,7],
         4:[5,6],
         5:[],
         6:[],
        7:[]}                           #taking graph in disctionary data type

visited = [];
queue = [];

def bfs(visited, queue, root):
    queue.append(root)                  #adding to queue
    visited.append(root)                #adding to visit
    while queue:                        #applying the while loop on queue
        m = queue.pop(0)                #poping the queue 1st node
        for adjoint in graph[m]:        #applying for loop on the node which is poped
            if adjoint not in visited:  #checking if the adjustant node is visited or not
                queue.append(adjoint)   #adding node to queue and visited if node is not visited 
                visited.append(adjoint)

    print(visited)                      #Printing the visited nodes which your dfs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

print("This is bfs demo")
bfs(visited, queue, 1)
