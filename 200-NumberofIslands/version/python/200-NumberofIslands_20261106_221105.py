# Last updated: 11/6/2026, 10:11:05 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5        
6        islands = 0
7        visited = set()
8        num_rows = len(grid)
9        num_columns = len(grid[0])
10
11        def dfs(r, c):
12            queue = collections.deque()
13            queue.append((r, c))
14            possible_moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
15            visited.add((r, c))
16
17            while queue:
18                r, c = queue.popleft()
19
20                for x, y in possible_moves:
21                    if ((r + x) in range(num_rows) and 
22                        (c + y) in range(num_columns) and 
23                        (r + x, c + y) not in visited and
24                        grid[r + x][c + y] == "1"):
25
26                        queue.append((r + x, c + y))
27                        visited.add((r + x, c + y))
28
29        for r in range(num_rows):
30            for c in range(num_columns):
31                if grid[r][c] == "1" and (r,c) not in visited:
32                    dfs(r, c)
33                    islands += 1
34        
35        return islands
36