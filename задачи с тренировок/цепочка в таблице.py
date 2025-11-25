import sys


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[1]*m for _ in range(n)]  # каждая клетка сама по себе цепочка длины 1

    # создаем список всех клеток с координатами и значением
    cells = [(a[i][j], i, j) for i in range(n) for j in range(m)]
    cells.sort()  # сортируем по значению

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for val, x, y in cells:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == val + 1:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

    # ответ — максимальная длина цепочки
    print(max(max(row) for row in dp))

    


if __name__ == '__main__':
    main()
