from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        rows = len(maze)
        cols = len(maze[0])
        start_row, start_col = entrance
        
     
        queue = deque([(start_row, start_col, 0)])
        
        
        maze[start_row][start_col] = '+'
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            curr_row, curr_col, dist = queue.popleft()
            
            for dr, dc in directions:
                r, c = curr_row + dr, curr_col + dc
                
                
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.':
                    
                   
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        return dist + 1
                    
                  
                    maze[r][c] = '+'
                    queue.append((r, c, dist + 1))
                    
        return -1