class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            answer = max(answer, self.dfs(grid, [i, 0]))

        return answer
        
    def dfs(self, grid: List[List[int]], start) -> int:
        max_count = 0

        m, n = len(grid), len(grid[0])
        
        visited = [[False] * n for _ in range(m)]
        visited[start[0]][start[1]] = True

        dist = [[0] * n for _ in range(m)]

        dx = [-1, 0, 1]
        dy = [1, 1, 1]

        stack = [start]
        while stack:
            x, y = stack.pop()

            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and visited[nx][ny] is False
                    and grid[x][y] < grid[nx][ny]
                ):
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    
                    stack.append([nx, ny])

                    if max_count < dist[nx][ny]:
                        max_count = dist[nx][ny]

        return max_count