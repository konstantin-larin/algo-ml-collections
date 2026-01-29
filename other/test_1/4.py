# дан неориентированный граф
# требуется сообщить длину наименьшего простого цикла в нем, или что цикла нет
# простой цикл это например граф 1 -2 -3-4 -1 то есть первая и последние вершины совпадают а остальные единожды
# колво вершин в графе 2 <= n <= 2500
# колво ребер в графе 1 <= m <= 5000
# вершины нумерованы от 1 до n
# важно - в графе нет петель и кратных ребер - это исключает каких-то неординарных случаев
# составим граф
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# так ну здесь dfs или bfs что-то типа того
# bfs находит простейший цикл (но не гарантировано минимальный)
# в целом так как вершин в худшем мб 2500 а времени 1 сек то успеем
INF = float('inf')
ans = INF
from collections import deque
for v in range(1, n + 1):    
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    dist[v] = 0    
    queue = deque([v])
    while queue:
        u = queue.popleft()
        if dist[u] * 2 + 1 >= ans: # если потенциальный цикл уже длинее найденного, то скип
            continue 
        for x in graph[u]:
            if dist[x] == INF: # не посещали
                dist[x] = dist[u] + 1
                parent[x] = u
                queue.append(x)
            elif parent[u] != x: # нашли цикл
                cycle_len = dist[u] + dist[x] + 1
                ans = min(ans, cycle_len)            
if ans == INF:
    print(-1)
else:
    print(ans)