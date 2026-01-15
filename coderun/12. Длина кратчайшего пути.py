import sys
from collections import deque


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    a, b = map(lambda x: int(x) - 1, input().split())

    dist = [-1] * n    
    dist[a] = 0

    queue = deque([a])
    while queue:
        v = queue.popleft()
        for u in range(n):
            if adj_matrix[v][u] == 1 and dist[u] == -1:
                dist[u] = dist[v] + 1                
                queue.append(u)                
    
    print(dist[b])


if __name__ == '__main__':
    main()
