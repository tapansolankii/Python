from collections import deque


def bfs_traversal(adjacency_matrix: list, startVerex: int) -> list:
    q = deque()
    visited_order_result = []
    visited = [False for i in range(len(adjacency_matrix))]
    
    q.append(startVerex)
    visited[startVerex] = True
    visited_order_result.append(startVerex)

    while q:
        currentVertex = q.popleft()
        for i in adjacency_matrix[currentVertex]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                visited_order_result.append(i)

    return visited_order_result



def add_edge(adjacency_matrix: list, a, b):
    adjacency_matrix[a].append(b)
    adjacency_matrix[b].append(a)



def main():
    vertices = 5
    adjacency_matrix = [[] for _ in range(vertices)]
    add_edge(adjacency_matrix, 0, 1)
    add_edge(adjacency_matrix, 0, 2)
    add_edge(adjacency_matrix, 1, 3)
    add_edge(adjacency_matrix, 1, 4)
    add_edge(adjacency_matrix, 2, 4)

    result = bfs_traversal(adjacency_matrix, 0)
    print(result)


if __name__ == "__main__":
    main()




# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\6_BFS_mine.py
# [0, 1, 2, 3, 4]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
