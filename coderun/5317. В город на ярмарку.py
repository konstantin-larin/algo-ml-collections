# https://coderun.yandex.ru/problem/new-year-fair/description
import sys
from collections import defaultdict


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())        
    graph = defaultdict(list) 
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    
    def dfs(v):
        stack = [v]
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                for w in graph[u]:
                    if not visited[w]:
                        stack.append(w)
    c = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            c += 1
    print(m - (n - c))    


if __name__ == '__main__':
    main()
