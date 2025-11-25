import sys
from collections import defaultdict, deque


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    graph = defaultdict(list) # {v1: [v2...v_n-1]}    
    deadlocks = set()

    n = int(input())
    for _ in range(n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)        
        graph[v2].append(v1)

        if len(graph[v1]) == 1:
            deadlocks.add(v1)
        if len(graph[v1]) == 2:
            deadlocks.remove(v1)
        if len(graph[v2]) == 1:
            deadlocks.add(v2)
        if len(graph[v2]) == 2:
            deadlocks.remove(v2)
    

    def multi_source_bfs(graph, sources):
        dist = {v: float('inf') for v in graph}
        origin = {}
        q = deque()

        # инициализация
        for s in sources:
            dist[s] = 0
            origin[s] = s
            q.append(s)

        pair_dist = {}  # кратчайшие пути между источниками

        min_d = float('inf')

        while q:
            v = q.popleft()
            for u in graph[v]:
                # если вершина ещё не посещена
                if dist[u] == float('inf'):
                    dist[u] = dist[v] + 1
                    origin[u] = origin[v]
                    q.append(u)
                # если встретились волны разных источников
                elif origin[u] != origin[v]:
                    a, b = sorted([origin[u], origin[v]])
                    d = dist[u] + dist[v] + 1
                    if (a, b) not in pair_dist or d < pair_dist[(a, b)]:
                        pair_dist[(a, b)] = d
                        min_d = min(min_d, d)

        return pair_dist, min_d
    

    return multi_source_bfs(graph, deadlocks)[1]






if __name__ == '__main__':
    print(main())
