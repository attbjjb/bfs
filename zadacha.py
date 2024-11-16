from collections import *
import sys

DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]

def handle_edge(x, y, dir, nx, ny, ndir):
    if dist[nx][ny][ndir] is None:
        dist[nx][ny][ndir] = dist[x][y][dir] + 1
        q.append((nx, ny, ndir))

n, m = map(int, input().split())
field = [input() for _ in range(n)]
q = deque()
dist = [[[None] * 4 for _ in range(m)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        if field[x][y] == 'S':
            dist[x][y][0] = 0
            q.append((x, y, 0))
while q:
    x, y, dir = q.popleft()
    if (x == 0 or x == n - 1) or (y == 0 or y == m - 1):
        print(dist[x][y][dir])
        sys.exit(0)
    handle_edge(x, y, dir, x, y, (dir + 1) % 4)
    handle_edge(x, y, dir, x, y, (dir + 3) % 4)
    nx = x + DX[dir]
    ny = y + DY[dir]
    if (0 <= nx < n and 0 <= ny < m and field[nx][ny] == '.'): handle_edge(x, y, dir, nx, ny, dir)

print(-1)





