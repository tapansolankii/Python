from collections import deque

# Function to add an edge between vertices x and y
def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

# Function to print the parent of each node
def printParents(node, adj, parent):
    # current node is Root, thus, has no parent
    if parent == 0:
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node, parent))

    # Using DFS
    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)

# Function to print the children of each node
def printChildren(Root, adj):
    # Queue for the BFS
    q = deque()
    # pushing the root
    q.append(Root)
    # visit array to keep track of nodes that have been
    # visited
    vis = [0] * len(adj)
    # BFS
    while q:
        node = q.popleft()
        vis[node] = 1
        print("{}->".format(node)),
        for cur in adj[node]:
            if vis[cur] == 0:
                print(cur),
                q.append(cur)
        print()

# Function to print the leaf nodes
def printLeafNodes(Root, adj):
    # Leaf nodes have only one edge and are not the root
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != Root:
            print(i)

# Function to print the degrees of each node
def printDegrees(Root, adj):
    for i in range(1, len(adj)):
        print(i, ":"),
        # Root has no parent, thus, its degree is equal to
        # the edges it is connected to
        if i == Root:
            print(len(adj[i]))
        else:
            print(len(adj[i]) - 1)

# Driver code
N = 7
Root = 1
# Adjacency list to store the tree
adj = [[] for _ in range(N + 1)]
# Creating the tree
addEdge(1, 2, adj)
addEdge(1, 3, adj)
addEdge(1, 4, adj)
addEdge(2, 5, adj)
addEdge(2, 6, adj)
addEdge(4, 7, adj)

print(f'The adj is {adj}')
print(f'The length of adj is {len(adj)}')

# Printing the parents of each node
print("The parents of each node are:")
printParents(Root, adj, 0)

# Printing the children of each node
print("The children of each node are:")
printChildren(Root, adj)

# Printing the leaf nodes in the tree
print("The leaf nodes of the tree are:")
printLeafNodes(Root, adj)

# Printing the degrees of each node
print("The degrees of each node are:")
printDegrees(Root, adj)



# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\12_Trees.py    
# The adj is [[], [2, 3, 4], [1, 5, 6], [1], [1, 7], [2], [2], [4]]
# The length of adj is 8
# The parents of each node are:
# 1->Root
# 2->1
# 5->2
# 6->2
# 3->1
# 4->1
# 7->4
# The children of each node are:
# 1->
# 2
# 3
# 4

# 2->
# 5
# 6

# 3->

# 4->
# 7

# 5->

# 6->

# 7->

# The leaf nodes of the tree are:
# 3
# 5
# 6
# 7
# The degrees of each node are:
# 1 :
# 3
# 2 :
# 2
# 3 :
# 0
# 4 :
# 1
# 5 :
# 0
# 6 :
# 0
# 7 :
# 0
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 