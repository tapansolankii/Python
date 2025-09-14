from collections import deque

# BFS from given source s
def bfs(adj, s):

    # Create a queue for BFS
    q = deque()
    
    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as 
    # visited
    visited = [False] * len(adj);
    print(f'Visited Initially: {visited}')

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
      
        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" Done one iteration ")
        print()
        # Get all adjacent vertices of the dequeued 
        # vertex. If an adjacent has not been visited, 
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]
    print(adj)
    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    print(f'the adjacency list initialised is: {adj}')
    bfs(adj, 0)



# Output
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\6_BFS.py
# [[], [], [], [], []]
# BFS starting from 0: 
# the adjacency list initialised is: [[1, 2], [0, 3, 4], [0, 4], [1], [1, 2]]
# Visited Initially: [False, False, False, False, False]
# 0 Done one iteration 
# 1 Done one iteration 
# 2 Done one iteration 
# 3 Done one iteration 
# 4 Done one iteration 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 