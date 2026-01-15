import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0,-1)]

    def dfs(i, j):
        stack = [(i, j)]
        visited[i][j] = True
        height = heights[i][j]
        is_sink = True
        while stack:
            ci, cj = stack.pop()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if heights[ni][nj] < height:
                        is_sink = False
                    elif heights[ni][nj] == height and not visited[ni][nj]:
                        visited[ni][nj] = True
                        stack.append((ni, nj))
        return is_sink
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                ans += int(dfs(i, j))
    print(ans)


if __name__ == '__main__':
    main()